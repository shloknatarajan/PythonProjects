# Imports
import tweepy
import time
import random
from config import consumer_key_1, consumer_secret_1, access_token_1, access_token_secret_1

# Authorizations for tweepy
auth1 = tweepy.OAuthHandler(consumer_key_1, consumer_secret_1)
auth1.set_access_token(access_token_1, access_token_secret_1)
api = tweepy.API(auth1)

# Methods
def follower_mine():
    users = tweepy.Cursor(api.followers, screen_name="IBMBlockchain", count = 50).items()
    count = 0
    for user in users:
        # Checks if followed previously
        with open("followed.txt.", "r") as followedFileRead:
            if (user.screen_name in followedFileRead):
                print("Duplicate, skipping")
                continue
            # followedFileRead closing

        # Follows and writes to followed doc provided previous conditions are met
        with open("prelim.txt", "a") as prelim:
            prelim.write(user.screen_name + "\n")
        
        count += 1

        # Pauses for random amount of time (between 0 and 1s) in between each follow
        #time.sleep(0.1 * random.randint(1, 10))

        # Stops after 1000 follows -- can set to anything you want
        if (count == 2000):
            break

    print("Finished following 1000 people")

def get_my_friends():
    f = open("followed.txt", "w")
    f.close()
    print("Getting friends\n")
    count = 0
    users = tweepy.Cursor(api.friends).items()
    for user in users:
        with open("followed.txt", "a") as followedFile:
            followedFile.write(user.screen_name + "\n")
            count += 1
            if (count % 100 == 0):
                break

def remove_non_followers():
    count = 0
    friends = tweepy.Cursor(api.friends).items()
    followers = tweepy.Cursor(api.followers).items()
    for f in friends:
        if f not in followers:
            api.destroy_friendship(f)
            count += 1
            if (count == 1000):
                break
    print("Removed " + str(count) + "nonfollowers")


# Code to run
try:
    follower_mine()
except tweepy.RateLimitError:
    print("Waiting for rate limit error to go away \n")
    time.sleep(15 * 60)    

# Checks if unfollowed previously -- Guess I don't really need this since the followed list will contain the unfollowed list
        # with open("unfollowed.txt", "r") as unfollowedFile:
        #    if (user.screen_name in unfollowedFile):
        #        print("Unfollowed previously, skipping")
        #        continue 