def start(mailSubject, mailContent, password, smtpServer):
    print("\n----------------------------")
    print("        Sending mail        ")
    print("----------------------------")
    import smtplib, ssl
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    email_from = 'contact@killianferrier.fr'
    email_to = ['killbibferrari@gmail.com']

    print("[SM] - Mail creation...")
    email_message = MIMEMultipart()
    email_message['From'] = email_from
    email_message['To'] = ' '.join(email_to)
    email_message['Subject'] = mailSubject
    email_message.attach(MIMEText(mailContent, 'plain'))
    email_string = email_message.as_string()
    print("[SM] - Mail creation complete")

    print("[SM] - Sending mail...")
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtpServer, 465, context=context) as server:
        print("[SM] - (msg) Connecting to the smtp server...")
        server.login(email_from, password)
        print("[SM] - (msg) Connection established")
        print("[SM] - (msg) Sending mail...")
        server.sendmail(email_from, email_to, email_string)
        print("[SM] - (msg) Mail send!")
    print("[SM] - Mail sending complete")

    print("")


def startHTML(mailSubject, mailContent, password, smtpServer):
    print("\n----------------------------")
    print("        Sending mail        ")
    print("----------------------------")
    import smtplib, ssl
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    email_from = 'contact@killianferrier.fr'
    email_to = ['killbibferrari@gmail.com']

    print("[SM] - Mail creation...")
    email_message = MIMEMultipart()
    email_message['From'] = email_from
    email_message['To'] = ' '.join(email_to)
    email_message['Subject'] = mailSubject
    email_message.attach(MIMEText(mailContent, "html"))
    email_string = email_message.as_string()
    print("[SM] - Mail creation complete")

    print("[SM] - Sending mail...")
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtpServer, 465, context=context) as server:
        print("[SM] - (msg) Connecting to the smtp server...")
        server.login(email_from, password)
        print("[SM] - (msg) Connection established")
        print("[SM] - (msg) Sending mail...")
        server.sendmail(email_from, email_to, email_string)
        print("[SM] - (msg) Mail send!")
    print("[SM] - Mail sending complete")

    print("")

