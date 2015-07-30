tftoptions = { 
	# API keys for your registered app. get them here: https://apps.twitter.com/
	'consumer_key' :	'',
	'consumer_secret' :	'',
	# settings for your first account. (this account will get tracked)
	'screen_name1' :	'',
	'access_token1' :	'',
	'access_token_secret1' :'',
	# settings for your second account. (this account will notify your first one via direct message)
	'screen_name2' :	'',
	'access_token2' :	'',
	'access_token_secret2' :'',
	# time between checks of follower and friend list in seconds. too many API requests could lead to error 429: api rate limit reached
	'check_intervall' :	'300',
	# set to '1' if you want to get a notification via direct message for the specific event
	'notify_unfollow' :	'1',
	'notify_follow' :	'1'	
}
