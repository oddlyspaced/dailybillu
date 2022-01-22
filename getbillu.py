# Fetches a random cat video link from youtube
# Search constraints :
# length = < 4 Minutes [ Short ]

from youtubesearchpython import *
import random
from config import Config

# Read random query from queries file
query = random.choice(open("queries", "r").readlines())
print(query)

cats = CustomSearch(query, Config.SEARCH_RESULT_DURATION, limit = Config.SEARCH_QUERY_LIMIT)

print(cats.result())