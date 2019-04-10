import tweepy

consumer_key = 'oPNczxdaUWTltpxy7QFwgmiVm'
consumer_secret = 'VeiJ7vHaEAGy0SmGT4SEYXaSZZicCtwx7cUJcTv3fAYHSKOyLh'
access_token = '2609087506-i2FKP0WHokcSl0PsPYIjp8TlL6VflNA26SVnFcU'
access_token_secret = 'CBMIuVRkjn3PSck9fl1EmKmu8NVFwCPPemxNjPDF1DlAx'

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)
public_tweets = api.home_timeline()

name="sajnanidipen98"
tweetCount = 3

results = api.user_timeline(id=name, count=tweetCount)
print("Fetching tweets from:",name)

for tweet in results:
   print (tweet.text)
