# Fetches a random cat video link from youtube
# Search constraints :
# length = < 4 Minutes [ Short ]

from nis import cat
from youtubesearchpython import *
import random
from config import Config

class Billu :
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

print(Billu().get_single_billu())