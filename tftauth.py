#! /usr/bin/env python

from tft_options import tftoptions
import webbrowser
import tweepy

CONSUMER_KEY = tftoptions['consumer_key']
CONSUMER_SECRET = tftoptions['consumer_secret']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
url = auth.get_authorization_url()
print(url)
webbrowser.open(url)
code = input('verification code: ').strip()
access_token = auth.get_access_token(verifier=code)

print('ACCESS_TOKEN: '+access_token[0])
print('ACCESS_TOKEN_SECRET: '+access_token[1])

