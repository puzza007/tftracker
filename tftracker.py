#! /usr/bin/env python

from twitterkeys import twitterkeys
import time
import tweepy

# account 1 is the account that gets tracked
# account 2 is the account that messages the first as notification

CONSUMER_KEY = twitterkeys['consumer_key']
CONSUMER_SECRET = twitterkeys['consumer_secret']
SCREEN_NAME1 = twitterkeys['screen_name1']
SCREEN_NAME2 = twitterkeys['screen_name2']
ACCESS_TOKEN1 = twitterkeys['access_token1']
ACCESS_TOKEN2 = twitterkeys['access_token2']
ACCESS_TOKEN_SECRET1 = twitterkeys['access_token_secret1']
ACCESS_TOKEN_SECRET2 = twitterkeys['access_token_secret2']

# authentificate first account as api1
print("authentificating first account...")
auth1 = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth1.set_access_token(ACCESS_TOKEN1, ACCESS_TOKEN_SECRET1)
api1 = tweepy.API(auth1)

#authentificate second account as api2
print("authentificating second account...")
auth2 = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth2.set_access_token(ACCESS_TOKEN2, ACCESS_TOKEN_SECRET2)
api2 = tweepy.API(auth2)

api2.send_direct_message(screen_name = SCREEN_NAME1, text = "unfollow tracker started.") 
print("tracker started...")

followers = api1.followers_ids(SCREEN_NAME1)

while True:
	followers_old = followers
	print("updating follower list")
	followers = api1.followers_ids(SCREEN_NAME1)
	print("comparing lists...")
	for f in followers_old:
		if f not in followers:
			print(f)
			api2.send_direct_message(screen_name = SCREEN_NAME1, text = "this user unfollowed you: @" + api1.get_user(f).screen_name)
	print("sleeping 5 minutes from now")
	time.sleep(300)


