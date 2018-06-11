# Imports
import tweepy
import time
import random
from config import consumer_key_2, consumer_secret_2, access_token_2, access_token_secret_2
# uses snakeresearcher2

# Authorizations for tweepy
auth = tweepy.OAuthHandler(consumer_key_2, consumer_secret_2)
auth.set_access_token(access_token_2, access_token_secret_2)
api = tweepy.API(auth)

#Prelim = open("prelim.txt", "r").readlines()
def one_follower_check(name):
    person = api.get_user(name)
    if(person.followers_count < 150):
        # print("User has less than 150 followers")
        # print(person.screen_name + " has " + str(person.followers_count) + " followers.")
        return False
    else:
        # print(person.screen_name + " has " + str(person.followers_count) + " followers (sufficient)")
        return True

def write_one_follower(name):
    if(one_follower_check(name) == True):
        with open("temp.txt", "a") as temp:
            temp.write(name)

def main():
    Prelim = open("prelim.txt", "r").readlines()
    for user in Prelim:
        write_one_follower(user)

main()


        


        
