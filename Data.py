import csv
import tweepy
from tokens import consumer_key, consumer_secret, access_token, access_token_secret

def parseTweet(tweet):
    """
    Parses relevant information from tweet
    tweet - Tweepy Status object
    returns [tweet.user.screen_name, tweet.text, tweet.place.full_name] 
    """
    tweet = tweet._json
    # pprint(tweet)
    return [tweet['created_at'], tweet['user']['screen_name'], tweet['text']] 



# Announce date: 2017-03-29
# Release date: 2017-04-21
# Future date: 2017-04-22

def main():

    # Tweepy setup
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    # Query to search
    query = "galaxy -rt s8"

    # Writes CSV until rate limit hit
    with open('results.csv', 'w') as f: 
        w = csv.writer(f)
        for tweet in tweepy.Cursor(api.search, q=query, lang="en").items():
            w.writerow(parseTweet(tweet))

main()