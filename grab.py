import tweepy
import sys 
import sqlite3 
from tweepy.streaming import StreamListener 
from tweepy import OAuthHandler 
from tweepy import Stream 
from textblob import TextBlob

'''
# Create connection with database to store tweets 
conn = sqlite3.connect('twitter.db')
c = conn.cursor()

def create_table():
	c.execute("")
	conn.commit()

create_table()
'''

#user_bg_color = bg_color

# Create tweet stream  

access_token = "N/A"
access_token_secret = "N/A"
consumer_key = "N/A"
consumer_secret = "N/A"

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

class StreamListener(tweepy.StreamListener):

	def on_status(self,status):
		# created = status.created_at
		description = status.user.description
		text = status.text		
		loc = status.user.location
		text = status.text
		coords = status.coordinates
		name = status.user.screen_name
		user_created = status.user.created_at
		followers = status.user.created_at
		id_str = status.id_str
		created = status.created_at
		retweets = status.retweet_count
		print(description, text, loc, text, coords, name, user_created, followers, id_str, created, retweets)

	def on_error(self, status_code):
		if status_code == 420: 
			return False



stream_listener = StreamListener()
stream = tweepy.Stream(auth=api.auth, listener=stream_listener)
stream.filter(track=["england soccer"])

