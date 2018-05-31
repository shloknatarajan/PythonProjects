#imports
import tweepy
import time
#variables
consumer_key = 'YQzo2dtygDyyzrAhkJpgr9Ycx'
consumer_secret = 'Awf6BJajzcM7IuksOEaAdoj2QQ4iyRJX7nTzUfenJQVpglAaxa'
access_token = '3023082786-CWPEKVAZbqtjYC4IN7azML2ivj9SAL49V9QHyfH'
access_token_secret = 'yb1n9t5c2QdJjHkKApx4je9pccCzhF8nXV0qG8kPAnvbJ'
followedFile = open("followed.txt", "a")
unfollowedFile = open("unfollowed.txt", "a")

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

followers = tweepy.Cursor(api.followers).items()

#for follower in followers:
    #print(follower.screen_name)
    #follower.follow()

users = tweepy.Cursor(api.followers, screen_name="IBMBlockchain", count = 200).items()
for user in users:
    #print(user.screen_name)
    followedFile.write(user.screen_name + "\n")
    #time.sleep(5)



