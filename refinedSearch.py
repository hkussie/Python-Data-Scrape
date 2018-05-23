import tweepy
import sys 
import sqlite3 
from tweepy.streaming import StreamListener 
from tweepy import OAuthHandler 
from tweepy import Stream 
from textblob import TextBlob


access_token = "922706023-Cy2i1lN7Yo29vFbLIfcNvzGiGrt4iuHGi2LK7oSZ"
access_token_secret = "YfTTcTsoMv5AsZ1JEjoFNcRzVFCl99U0pVv88Ggg3uQSi"
consumer_key = "4qKSiJnzn02TqvC0vgsKNwNjV"
consumer_secret = "6THsxXRQcs3nCSacMRPeTl1EJn9qXdZo1RKZK6dAmhZFxapFcD"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

tweets = tweepy.Cursor(api.search, q="world cup", lan="English").items(100)
for tweet in tweets: 
	created = tweet.created_at
	description = tweet.user.description
	location = tweet.user.location
	text = tweet.text
	coordinates = tweet.coordinates
	name = tweet.user.screen_name 
	print(created, description, location, text, coordinates, name)
	
'''

tweets = tweepy.Cursor(api.search, q="iran", lan="English").items(100)
for tweet in tweets:
	print(tweet.retweet_count)
	# result = TextBlob(tweet.text)

for tweet in tweets:
	print()


for tweet in tweets:
	print()
'''
'''
tweet_polarity = TextBlob("This is an effin string, you loser, you suck I hate it!")
print(tweet_polarity.sentiment)
'''
