'''
Author: Paul Owe
Description: This is a twitter client that handles authentication to twitter via tweepy API.
For authentication you will need API keys from twitter. You can apply here https://developer.twitter.com/en
Note: Keep these keys private.
Last updated: Mar 4, 2021
'''
import os
import sys
from tweepy import API
from tweepy import OAuthHandler
from dotenv import load_dotenv

def get_twitter_auth():
    #set up twitter authentication

    # Return: tweepy.OAuthHandler object

    try:
        load_dotenv()
        access_secret = "gjxpdHcVwVT4G7aGBMz654DLHk1aVu1zBXVTohMifq2XU"
        access_token = "922977192-jzCCOIHFYh8Fs9N5DjlxZfW6CxgtLzPZyohYuqTX"
        consumer_secret = "pCmBTZ6dBqCaf1BTffkF8il0AAiWIhgUlYhhZ7jDZFMFuDyNa5"
        consumer_key = "bPIKaiR4d91amYlft7s6p39Nz"

    except KeyError:
        sys.stderr.write("TWITTER_* environment variables not set\n")
        sys.exit(1)
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    return auth


def get_twitter_client():
    #Setu twitter API client.

    # Return tweepy.API object

    auth = get_twitter_auth()
    client = API(auth)
    return client