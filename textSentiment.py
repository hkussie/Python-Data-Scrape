from textblob import TextBlob  
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()


'''
sentence = "This is a sentence, what are you gonna do about it? Answer or I'll hate you"
sentiment = TextBlob(sentence)
sentiment = sentiment.words

print(sentiment)
'''
'''
tweets = open("iran_data.txt", "r")
for tweet in tweets: 
	print(tweet), 
	sentiment = TextBlob(tweet)
	print("\n\t" + str(sentiment))
'''

