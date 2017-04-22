import csv
import tweepy
import nltk
import pandas as pd
from tokens import consumer_key, consumer_secret, access_token, access_token_secret
from pprint import pprint
import json

def parseTweet(tweet):
    """
    Parses relevant information from tweet
    tweet - Tweepy Status object
    returns [tweet.user.screen_name, tweet.text, tweet.place.full_name] 
    """
    tweet = tweet._json
    # pprint(tweet)
    return [tweet['created_at'], tweet['user']['screen_name'], tweet['text']] 

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# tweets = []
# for p in range(1, 1000):
#     print('Page', p, end='\r', sep='\t')
#     query = "-rt @united since:2017-04-08 until:2017-04-08"
#     try:
#         results = api.search(query, rpp=100, since_id=0)
#         print(results)
#         for tweet in results:
#             parsedTweet = parseTweet(results)
#             tweets.append(parsedTweet)
#     except Exception as e:
#         print('\nError:', e, sep='\t')
#         break

# Announce date: 2017-03-29
# Release date: 2017-04-21
# Future date: 2017-04-22

tweets = []
query = "galaxy -rt s8"
date1 = "2017-03-29"
date2 = "2017-03-30"

last = None
results = tweepy.Cursor(api.search, q = query, since = date1, until = date2, lang = "en").items()
for tweet in results:
    print(tweet(parseTweet))


print("Tweets", len(tweets), sep='\t')
with open('results.csv', 'w') as f:
    w = csv.writer(f)
    w.writerows(tweets)