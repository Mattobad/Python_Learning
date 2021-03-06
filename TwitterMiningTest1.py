"""
NLP(Natural Language Processing )
Tweeter mining for user and tweets
"""

"""
importing tweepy and adding our authentication
"""

import tweepy

consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret =""

# Creating API object

# Creating auth object
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)

#Creating access token and secret
auth.set_access_token(access_token,access_token_secret)

# Creating the API object by passing auth
api = tweepy.API(auth)

# Using the API object to get tweets from your timeline, and storing it in a variable called public_tweets

public_tweets = api.home_timeline()
# foreach through all tweets pulled
for tweet in public_tweets:
   # printing the text stored inside the tweet object
   print ("Location of tweeter ",tweet.user.location)
   print("Tweeter name ",tweet.user.screen_name)
   
   
   

"""
Tweets from specific users
"""


# Creating the API object while passing in auth information
api = tweepy.API(auth)

# The Twitter user who we want to get tweets from
name = "nytimes"
# Number of tweets to pull
tweetCount = 20

# Calling the user_timeline function with our parameters
results = api.user_timeline(id=name, count=tweetCount)

# foreach through all tweets pulled
for tweet in results:
   # printing the text stored inside the tweet object
   print (tweet.text)
   


"""
Finding Tweets using keywords
"""

# Creating the API object while passing in auth information
api = tweepy.API(auth)

# The search term you want to find
query = "Toptal"
# Language code (follows ISO 639-1 standards)
language = "en"

# Calling the user_timeline function with our parameters
results = api.search(q=query, lang=language)

# foreach through all tweets pulled
for tweet in results:
   # printing the text stored inside the tweet object
   print (tweet.user.screen_name,"Tweeted:",tweet.text)
