import smtplib, ssl
from threading import local
from config import Config
from os.path import exists
from youtubesearchpython import *
import random

# Fetches a random cat video link from youtube
class GetBillu :
    def __init__(self) :
        pass

    # Check if id is present
    def already_used(self, id) :
        # TODO : Check if used file exts
        f = open("used", "r")
        all_ids = f.readlines()
        f.close()
        return id in all_ids

    def save_billu(self, id) :
        f = open("used", "w+")
        f.write(id)
        f.close()

    def get_single_billu(self) :
        # Read random query from queries file
        query = random.choice(open("queries", "r").readlines())
        # Search for billu videos
        cats = CustomSearch(query, Config.SEARCH_RESULT_DURATION, limit = 1)
        # Check if we already used the id
        print(cats.result()['result'][0]["id"])
        while self.already_used(cats.result()['result'][0]["id"]) is True:
            cats.next()
        
        # new billu found
        # save it and return link
        self.save_billu(cats.result()['result'][0]["id"])
        return cats.result()['result'][0]["link"]

# Generates Email Content
class MeowSays :
    greetings = ["Meow", "Meow Meow", "Meowww"]
    opening = ["Meow", "Meow Meow!", "Meow Meow Meow!"]
    body = ["Meow Meow Meow Meow Meow ₍⸍⸌̣ʷ̣̫⸍̣⸌₎", "Meow Meow Meow 👍", "Meow Meow 😽", "Meow Meow Meow! ☀️"]
    regards = ["Meow,"]
    name = ["Meow"]
    sign = ["/ᐠ｡ꞈ｡ᐟ\\", " /ᐠ｡‸｡ᐟ\\", " /ᐠ｡ꞈ｡ᐟ✿\\"]
    def __init__(self) :
        pass

    def say(self) :
        msg = random.choice(self.greetings) + ",\n" + random.choice(self.opening) + "\n\n" + random.choice(self.body) + "\n\n" + random.choice(self.regards) + "\n" + random.choice(self.name) + "\n" + random.choice(self.sign)
        return msg

def get_day_count() :
    if exists("day") == False :
        day = 1
        f = open("day", "w+")
        f.write("1")
        f.close()
    else :
        # read day number
        f = open("day", "r")
        day = int(f.readline())
        f.close()
    return int(day)

def update_day_count() :
    # update day number for next day
    f = open("day", "w")
    f.write(str(get_day_count() + 1))
    f.close()

message = """\
Subject: Daily Billu - Day """ + str(get_day_count()) + """

""" + MeowSays().say() + "\n\n" + GetBillu().get_single_billu()

# open server and send mail
context = ssl.create_default_context()
with smtplib.SMTP(Config.SMTP_SERVER, Config.SMTP_PORT) as server:
    server.starttls(context = context)
    server.login(Config.CLIENT_EMAIL, Config.CLIENT_PASSWORD)
    for receiver in Config.RECEIVER_EMAIL :
        server.sendmail(Config.CLIENT_EMAIL, receiver, message.encode('utf-8'))

update_day_count()