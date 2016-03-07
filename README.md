# TFTracker
Twitter (un)Follower Tracker

A bot for Twitter, based on [Tweepy](https://github.com/tweepy/tweepy), that tracks follows and unfollows and notifies you via direct message about it. You can either get notified via direct messages to yourself (seems to get marked as read on some clients instantly) or via a second account, that sends you notifications via direct message.

### Install

You have to install [Tweepy](https://github.com/tweepy/tweepy) to use this. Register a new Twitter App [here](https://apps.twitter.com/) and add your consumer keys to [tft_options.py](tft_options.py). After that you can get the access tokens for your accounts using [tftauth.py](tftauth.py). Be sure that you are logged into the right account, before doing this.

### Usage
I'd recommend to set the interval in [tft_options.py](tft_options.py) to 0 and start it via cron in any interval you want.

You could also start it like this, using screen, to leave it running in the background and use TFTrackers interval function, but it seems that it crashes from time to time.
```bash
screen -dmS tftracker python tftracker.py
```

Don't set the interval to low, because of Twitters API limits.
