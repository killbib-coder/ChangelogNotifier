import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class Mail():
    def __init__(self) -> None:
        self.smtp_server = ''
        self.smtp_password = ''
        self.mail_from = ''
        self.mail_to = ''
        self.mail_subject = ''
        self.mail_content = ''
        self.mail_message = ''

    def sendMail(self):
        mail_message = MIMEMultipart()
        mail_message['From'] = self.mail_from
        mail_message['To'] = self.mail_to # ' '.join(Mail.mailTo)
        mail_message['Subject'] = self.mail_subject
        mail_message.attach(MIMEText(self.mail_content, 'html'))
        mailString = mail_message.as_string()
        self.mail_message = mailString
        print("[+] SendMail - Mail creation complete")
        context = ssl.create_default_context()
        try :
            with smtplib.SMTP_SSL(self.smtp_server, 465, context=context) as server:
                server.login(self.mail_from, self.smtp_password)
                server.sendmail(self.mail_from, self.mail_to, self.mail_message)
            print("[+] SendMail - Mail sending complete")
        except smtplib.SMTPAuthenticationError:
            raise Exception("[-] SendMail - Échec de l'authentification. Vérifie ton nom d'utilisateur et ton mot de passe SMTP.")
        except smtplib.SMTPException as e:
            # Autres erreurs liées à SMTP
            raise Exception(f"[-] SendMail - Erreur lors de la communication avec le serveur SMTP : {e}")
