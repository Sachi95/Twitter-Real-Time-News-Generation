import requests
import twitter
import json
import urllib2
from prettytable import PrettyTable
proxies={
  "http":"http//172.31.1.3:8080"
}
CONSUMER_KEY = 'iztkswCNNPPmaJAfe7u9DCBfH'
CONSUMER_SECRET = 'x1nUUpUKVYKe3Wk6PAt2nPA71IzHDkid4fPGD9MO0qqCU6XKb3'
OAUTH_TOKEN = '4789947481-GC5GUChGtJEX5MRca8rXhYAbuXBJUh6TBS3dloj'
OAUTH_TOKEN_SECRET = 'sYhefInJtzknCmDFtNVLVoC2fGhGAqZFUxjpnJvZZng7a'

auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

twitter_api = twitter.Twitter(auth=auth)

WORLD_WOE_ID = 1
US_WOE_ID = 23424977
IND_WOE_ID = 23424848

world_trends = twitter_api.trends.place(_id=WORLD_WOE_ID)
us_trends = twitter_api.trends.place(_id=US_WOE_ID)
india_trends = twitter_api.trends.place(_id=IND_WOE_ID)

world_trends = [trend['name'] for trend in world_trends[0]['trends']]
us_trends = [trend['name'] for trend in us_trends[0]['trends']]
india_trends = [trend['name'] for trend in india_trends[0]['trends']]

pt = PrettyTable(field_names=['World Trends', 'US Trends', 'India Trends'])

for world_trend, us_trend, india_trend in zip(world_trends, us_trends, india_trends):
   pt.add_row([world_trend, us_trend, india_trend])

print pt
