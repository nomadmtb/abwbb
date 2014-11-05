#!/usr/bin/python
# Twitter.py: Class that wraps the functionality of the Tweepy API.

import tweepy
from AppPanic import panic
from time import sleep
import os
import threading


class Twitter():

    # Init the latest @reply.
    def init_reply_context(self):

        try:
            self.reply_context = self.api_conn.mentions_timeline()[0].id
        except:
            panic("Error", "Can't access context")

        print("Successfully added context with reply {0}".format(self.reply_context))

    #Constructor...
    def __init__(self):

        # Load the access keys.
        try:
            with open('access_keys.txt') as access_file:

                items = access_file.readlines()
                self.consumer = items[0].rstrip()
                self.consumer_secret = items[1].rstrip()
                self.access = items[2].rstrip()
                self.access_secret = items[3].rstrip()
        except:
            panic("Error", "Can't access access_keys.txt")

        # Apply the application keys to our Tweepy instance.
        authentication = tweepy.OAuthHandler(self.consumer, self.consumer_secret)
        authentication.set_access_token(self.access, self.access_secret)

        # Authenticate us with twitter.
        self.api_conn = tweepy.API(authentication)

        # Init the latest @reply.
        self.reply_context = 0
        self.init_reply_context()

    # Start the monitoring for @reply
    def start_monitor(self):

        while True:

            # This list will hold the new @reply's with each iteration.
            new_statuses = []

            # We only want to check every n seconds.
            sleep(30)

            # Try to get the new statuses with the current context.
            try:
                new_statuses = self.api_conn.mentions_timeline(since_id=self.reply_context)
            except:
                panic("Error", "Can't get new mentions with current context")

            # Print notification message if there are no new @reply's
            if len(new_statuses) == 0:
                print("No new @reply's detected")

            else:
                # Play sound from shell.
                os.system("afplay sounds/Tune.m4a &")

                # Iterate through the statuses and print them.
                for status in new_statuses:
                    print("@{0}: {1}".format(status.author.screen_name, status.text))

                    # Update our new context for subsequent requests.
                    print("Successfully updated context with reply {0}".format(new_statuses[-1].id))
                    self.reply_context = new_statuses[-1].id
