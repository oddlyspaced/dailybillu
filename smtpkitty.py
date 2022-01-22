import smtplib, ssl

port = 587
smtp_server = "smtp.gmail.com"
sender_email = "***"
receiver_email = "***"
password = input("Enter password of dailybillu:")
message = """\
Subject: Hi there

This message is sent from Python."""

context = ssl.create_default_context()
with smtplib.SMTP(smtp_server, port) as server:
    server.starttls(context=context)
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
