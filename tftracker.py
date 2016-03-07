#! /usr/bin/env python

from tft_options import tftoptions
import time
import tweepy
import pickle

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
NOTIFY_UNFRIEND = tftoptions['notify_unfriend']
NOTIFY_FRIEND = tftoptions['notify_friend']

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

followersfile = open('followers.dump', 'wb')
pickle.dump(followers, followersfile)
followersfile.close()
friendsfile= open('friends.dump', 'wb')
pickle.dump(friends, friendsfile)
friendsfile.close()

while True:
	# follower list tracking
	if NOTIFY_FOLLOW == '1' or NOTIFY_UNFOLLOW == '1': # check if updating follower list ist necessary to reduce api calls

		followersfile = open('followers.dump', 'rb')
		followers_old = pickle.load(followersfile)
		followersfile.close()

		print("updating follower list")
		followers = api1.followers_ids(SCREEN_NAME1)
		print("comparing lists...")
		if NOTIFY_UNFOLLOW == '1':
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

		followersfile = open('followers.dump', 'wb')
		pickle.dump(followers, followersfile)
		followersfile.close()

	# friend list tracking
	if NOTIFY_FRIEND == '1' or NOTIFY_UNFRIEND == '1': # check if updating friend list is necessary to reduce api calls

		friendsfile = open('friends.dump', 'rb')
		friends_old = pickle.load(friendsfile)
		friendsfile.close()

		print('updating friends list')
		friends = api1.friends_ids(SCREEN_NAME1)
		print('comparing lists...')
		if NOTIFY_UNFRIEND == '1':
			for f in friends_old:
				if f not in friends:
					f_name = api1.get_user(f).screen_name
					print(f_name+' unfriended.')
					api2.send_direct_message(screen_name= SCREEN_NAME1, text = 'you unfollowed @'+f_name+'.')
		if NOTIFY_FRIEND == '1':
			for f in friends:
				if f not in friends_old:
					f_name = api1.get_user(f).screen_name
					print(f_name+' friended.')
					api2.send_direct_message(screen_name= SCREEN_NAME1, text = 'you followed @'+f_name+'.')

		friendsfile= open('friends.dump', 'wb')
		pickle.dump(friends, friendsfile)
		friendsfile.close()

	print('sleeping '+ str(CHECK_INTERVALL) +'s from now.')
	time.sleep(CHECK_INTERVALL)

