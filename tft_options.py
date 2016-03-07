tftoptions = { 
	# time between checks of follower and friend list in seconds. too many API requests could lead to error 429: api rate limit reached
	# set it to 0 to disable interval functionality (e.g. to use it with cron)
	'check_intervall' :	'0',
	# set to '1' if you want to get a notification via direct message for the specific event
	'notify_unfollow' :	'1',
	'notify_follow' :	'1',
	'notify_unfriend' :	'1',
	'notify_friend' :	'1',
	# use this option to get notified from ur first account via DM, seconds for second account will be ignored
	'one_acc_mode' :	'1',


	# API keys for your registered app. get them here: https://apps.twitter.com/
	'consumer_key' :	'',
	'consumer_secret' :	'',
	# settings for your first account, which will get tracked
	'screen_name1' :	'',
	'access_token1' :	'',
	'access_token_secret1' :'',
	# settings for your second account, which will notify your first one via DM, if one_acc_mode=0
	'screen_name2' :	'',
	'access_token2' :	'',
	'access_token_secret2' :''
}
