import smtplib, ssl
from config import Config
from getbillu import GetBillu

# ready day number
f = open("day", "r")
day = int(f.readline())
f.close()

# prepare message
message = """\
Subject: Daily Billu - Day """ + str(day) + """

Meow,
Meow meow!
Meow Meow Meow Meow.

Meow,
Meow

""" + GetBillu().get_single_billu()

# open server and send mail
context = ssl.create_default_context()
with smtplib.SMTP(Config.SMTP_SERVER, Config.SMTP_PORT) as server:
    server.starttls(context = context)
    server.login(Config.CLIENT_EMAIL, Config.CLIENT_PASSWORD)
    for receiver in Config.RECEIVER_EMAIL :
        server.sendmail(Config.CLIENT_EMAIL, receiver, message)

# update day number for next day
f = open("day", "w")
f.write(str(day+1))
f.close()