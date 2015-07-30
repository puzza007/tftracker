# TFTracker
Twitter (un)Follower Tracker

A bot for Twitter, based on [Tweepy](https://github.com/tweepy/tweepy), that tracks follows and unfollows and notifies you via direct message about it. You will need a second Twitter account, to get the notifications via direct message from TFTracker.

### Install

You have to install [Tweepy](https://github.com/tweepy/tweepy) to use this. Register a new Twitter App [here](https://apps.twitter.com/) and add your consumer keys to [tft_options.py](tft_options.py). After that you can get the access tokens for your accounts using [tftauth.py](tftauth.py). Be sure that you are logged into the right account, before doing this.

### Usage

I'd recommend to start the script with screen like this, to leave it running in the background:
```bash
screen -dmS tftracker python tftracker.py
```
