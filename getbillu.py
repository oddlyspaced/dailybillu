# Fetches a random cat video link from youtube
from youtubesearchpython import VideosSearch

cats = VideosSearch('cat small baby', limit = 10)

print(cats.result())