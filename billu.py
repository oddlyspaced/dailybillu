import smtplib, ssl
from config import Config

message = """\
Subject: Hi there

This message is sent from Python."""

context = ssl.create_default_context()
with smtplib.SMTP(Config.SMTP_SERVER, Config.SMTP_PORT) as server:
    server.starttls(context = context)
    server.login(Config.CLIENT_EMAIL, Config.CLIENT_PASSWORD)
    for receiver in Config.RECEIVER_EMAIL :
        server.sendmail(Config.CLIENT_EMAIL, receiver, message)