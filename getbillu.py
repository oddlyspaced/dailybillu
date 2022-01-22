# Fetches a random cat video link from youtube
# Search constraints :
# length = < 4 Minutes [ Short ]

from youtubesearchpython import *
import random

# Read random query from queries file
query = random.choice(open("queries", "r").readlines())
print(query)

cats = CustomSearch(query,  VideoDurationFilter.short, limit = 10)

print(cats.result())