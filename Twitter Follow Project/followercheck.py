# Imports
import tweepy
import time
import random
from config import consumer_key_2, consumer_secret_2, access_token_2, access_token_secret_2
# uses snakeresearcher2

# Authorizations for tweepy
auth2 = tweepy.OAuthHandler(consumer_key_2, consumer_secret_2)
auth2.set_access_token(access_token_2, access_token_secret_2)
api = tweepy.API(auth2)

Prelim = open("prelim.txt", "r").readlines()

def follower_check():
    index = 0
    # Converts screen name doc to a python list
    for user in Prelim:
        person = tweepy.api.get_user(user)
        if (person.followers_count < 150):
            del(Prelim[index])
            print("deleting person")
        else:
            print(person.screen_name + "has " + person.followers_count + " so they will not be removed \n")
            index += 1
    
def write_to_temp():
    # Writes sorted list to a temp file
    with open("temp.txt", "w") as temp:
        for user in Prelim:
            temp.write(user)
        
try:
    follower_check()
    print("Finished check. Writing to temp")
    write_to_temp()
except:
    print("writing to temp prematurely")
    write_to_temp()

        
