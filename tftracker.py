#! /usr/bin/env python

from tft_options import tftoptions
import time
import tweepy

# account 1 is the account that gets tracked
# account 2 is the account that messages the first as notification

CONSUMER_KEY = tftoptions['consumer_key']
CONSUMER_SECRET = tftoptions['consumer_secret']
SCREEN_NAME1 = tftoptions['screen_name1']
ACCESS_TOKEN1 = tftoptions['access_token1']
ACCESS_TOKEN_SECRET1 = tftoptions['access_token_secret1']
SCREEN_NAME2 = tftoptions['screen_name2']
ACCESS_TOKEN2 = tftoptions['access_token2']
ACCESS_TOKEN_SECRET2 = tftoptions['access_token_secret2']
CHECK_INTERVALL = float(tftoptions['check_intervall'])
NOTIFY_UNFOLLOW = tftoptions['notify_unfollow']
NOTIFY_FOLLOW = tftoptions['notify_follow']

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

api2.send_direct_message(screen_name = SCREEN_NAME1, text = 'TFTracker started. CHECK_INTERVALL='+ str(CHECK_INTERVALL) +'s. NOTIFY_FOLLOW='+NOTIFY_FOLLOW+'. NOTIFY_UNFOLLOW='+NOTIFY_UNFOLLOW+'.') 
print("tracker started...")

followers = api1.followers_ids(SCREEN_NAME1)
friends = api1.friends_ids(SCREEN_NAME1)

while True:
	# follower list tracking
	followers_old = followers
	print("updating follower list")
	followers = api1.followers_ids(SCREEN_NAME1)
	print("comparing lists...")
	for f in followers_old:
		if f not in followers:
			f_name = api1.get_user(f).screen_name
			print(f_name+' unfollowed.')
			api2.send_direct_message(screen_name = SCREEN_NAME1, text = "this user unfollowed you: @"+f_name)
	for f in followers:
		if f not in followers_old:
			f_name = api1.get_user(f).screen_name
			print(f_name+' followed.')
			api2.send_direct_message(screen_name = SCREEN_NAME1, text = "this user followed you: @"+f_name)

	# friend list tracking
	friends_old = friends
	print('updating friends list')
	friends = api1.friends_ids(SCREEN_NAME1)
	print('comparing lists...')
	for f in friends_old:
		if f not in friends:
			f_name = api1.get_user(f).screen_name
			print(f_name+' unfriended.')
			api2.send_direct_message(screen_name= SCREEN_NAME1, text = 'you unfollowed @'+f_name+'.')
	for f in friends:
		if f not in friends_old:
			f_name = api1.get_user(f).screen_name
			print(f_name+' friended.')
			api2.send_direct_message(screen_name= SCREEN_NAME1, text = 'you followed @'+f_name+'.')

	print('sleeping '+ str(CHECK_INTERVALL) +'s from now.')
	time.sleep(CHECK_INTERVALL)


