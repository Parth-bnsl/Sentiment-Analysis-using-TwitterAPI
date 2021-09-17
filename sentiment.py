from textblob import TextBlob
import tweepy
import re
import sys

keys = open('twitterapi.txt', 'r').read().splitlines()
# add api keys here
api_key = keys[0]
api_key_secret = keys[1]
access_token = keys[2]
access_token_secret = keys[3]

auth_handler = tweepy.OAuthHandler(consumer_key=api_key, consumer_secret=api_key_secret)
auth_handler.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth_handler)

search_term = 'Tesla'
tweet_amount = 50

tweets = tweepy.Cursor(api.search, q=search_term, lang='en').items(tweet_amount)

tweet_text = []
polarity = 0
positive = 0
neutral = 0
negative = 0
for tweet in tweets:
    temp = tweet.text.lower()
    temp = re.sub("@[A-Za-z0-9_]+", "", temp)
    temp = re.sub("#[A-Za-z0-9_]+", "", temp)
    temp = re.sub(r"http\S+", "", temp)
    temp = re.sub(r"www.\S+", "", temp)
    temp = re.sub('[()!?]', ' ', temp)
    temp = re.sub('\[,.*?\]', ' ', temp)
    temp = re.sub('rt : ', '', temp)
    temp = temp.replace("'","")
    temp = temp.replace(",","")
    analysis = TextBlob(temp)
    tweet_analysis = analysis.polarity
    if tweet_analysis > 0.00:
        positive += 1
    elif tweet_analysis == 0.00:
        neutral += 1
    else:
        negative += 1
    polarity += analysis.polarity

print(f"Amount of positive tweets: {positive}")
print(f"Amount of Negative tweets: {negative}")
print(f"Amount of Neutral tweets: {neutral}")