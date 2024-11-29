from database_manager import DatabaseManager
import json
import send_mail as sm
import scraper

db_manager = DatabaseManager()

tools = db_manager.get_all_tools()
users = db_manager.get_all_users()

tools_updated = []

def setMailParameters():
    mail = sm.Mail()
    with open('.config.json', 'r') as config_file:
        config_data = json.load(config_file)
    mail.smtp_server, mail.smtp_password, mail.mail_from = config_data.get('smtp', {}).get('server'), config_data.get('smtp', {}).get('password'), config_data.get('smtp', {}).get('from')
    return mail

if __name__ == "__main__":
    for tool in tools:
        if scraper.scrap(tool) != None :
            db_manager.update_tool(tool)
            tools_updated.append(tool.id)

    mail = setMailParameters()

    for user in users :
        tool_to_send = 0
        mail.mail_to = user.email
        html_content = "List of new changelogs for :<br>"

        for tool_id in db_manager.get_tool_ids_by_user(user.id):
            if tool_id in tools_updated:
                tool = db_manager.get_tool_by_id(tool_id)
                html_content += f'New version of <b>{tool.name}</b> : <a href="{tool.link}">{tool.version}</a><br>'
                tool_to_send +=1

        mail.mail_subject = f"Notification of {tool_to_send} new changelogs"

        if tool_to_send > 0:
            mail.mail_content = html_content
            mail.sendMail()
            print(f"[+] Main - Changelogs are sent to {user.email}")
        else:
            print(f"[+] Main - all changelogs are send to {user.email} ")
