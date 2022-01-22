# Fetches a random cat video link from youtube
# Search constraints :
# length = < 4 Minutes [ Short ]

from youtubesearchpython import *

cats = CustomSearch('cat small baby',  VideoDurationFilter.short, limit = 10)

print(cats.result())