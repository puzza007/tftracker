# TFTracker
Twitter (un)Follower Tracker

A bot for Twitter, based on [tweepy](https://github.com/tweepy/tweepy), that tracks unfollows and notifies you via direct message about it. For now it notifies about unfollows, if the user was following for more than five minutes (or any other time between the checks, you set). You will need a second Twitter account, to get the notifications via direct message from TFTracker.

Work in progress. More features will be added soon.

You have to install [Tweepy](https://github.com/tweepy/tweepy) to use this. Add your API keys to [twitterkeys.py](twitterkeys.py). [This script](https://github.com/tweepy/examples/blob/master/oauth/getaccesstoken.py) could be helpfull. A function like this will be added to TFTracker later.

I'd recommend to start this script with screen like this, to leave it running in the background:
```bash
screen -dmS tftracker python tftracker.py
```
You can adjust the sleep time (time between followerlist comparisons) manually. (A global option for this will be added soon.)
