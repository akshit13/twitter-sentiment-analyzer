import tweepy 
from textblob import TextBlob

consumerKey = ''
consumerSecret = ''

accessToken = ''
accessTokenSecret = ''

auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(accessToken, accessTokenSecret)

api = tweepy.API(auth)

publicTweet = api.search('')

for tweet in publicTweet:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment)