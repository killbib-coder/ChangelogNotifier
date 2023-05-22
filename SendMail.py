def start(mailSubject, mailContent, password, smtpServeur):
    print("----------------------------")
    print("        Sending mail        ")
    print("----------------------------")
    import smtplib, ssl
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    email_from = 'contact@killianferrier.fr'
    email_to = ['killbibferrari@gmail.com'] 

    print("[SM] - Création du mail...")
    email_message = MIMEMultipart()
    email_message['From'] = email_from
    email_message['To'] = ' '.join(email_to) #','.join(email_to)
    email_message['Subject'] = mailSubject
    email_message.attach(MIMEText(mailContent, 'plain'))
    email_string = email_message.as_string()
    print("[SM] - Fin de la création du mail")

    print("[SM] - Envoie du mail...")
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtpServeur, 465, context=context) as server:
        print("[SM] - (msg) Connexion au serveur smtp...")
        server.login(email_from, password)
        print("[SM] - (msg) Connexion établie")
        print("[SM] - (msg) Envoie du mail...")
        server.sendmail(email_from, email_to, email_string)
        print("[SM] - (msg) Mail envoyé!")
    print("[SM] - Fin de l'envoie du mail")

    print("")
