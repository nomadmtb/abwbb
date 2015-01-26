#!/usr/bin/python
# TwitterStream.py: This is the streaming implementation for the application.

from AppPanic import panic
import tweepy
import os
import signal
import random


class TwitterStream(tweepy.StreamListener):

    def __init__(self):

        # Start the tweet_count.
        self.tweet_count = 0

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
        self.authentication = tweepy.OAuthHandler(self.consumer, self.consumer_secret)
	self.authentication.secure = True
        self.authentication.set_access_token(self.access, self.access_secret)
        self.api = tweepy.API(self.authentication)

	# Print out current auth username for testing.
	print(self.api.me().name)

        # Store our terms that we will be looking for.
        self.stream_tags = ['@abwbb']

        # Call the super class init method.
        super(TwitterStream, self).__init__()

    # Use this function to start our stream.
    def start_stream(self):

        # Start the stream. Self is the delegate.
        streaming_api = tweepy.Stream(self.authentication, self)
        streaming_api.filter(track=self.stream_tags)

    # What we do when the class gets a status from the stream.
    def on_status(self, status):

	status_text = status.text.encode("utf-8")

        # Increment the counter.
        self.tweet_count += 1

        # Play the sound.
        os.system("afplay sounds/Tune.m4a &")

        # Print the details.
        print("[{0}]{1}:\t{2}".format(
            self.tweet_count,
            status.user.screen_name.encode("utf-8"),
            status.text.encode("utf-8"))
        )

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
        self.authentication = tweepy.OAuthHandler(self.consumer, self.consumer_secret)
	self.authentication.secure = True
        self.authentication.set_access_token(self.access, self.access_secret)
        self.api = tweepy.API(self.authentication)

	response = ""
	file = ""

	if "jaredism" in status_text.lower():
		file = "jaredisms.txt"
	else:
		file = "insults.txt"

	# Get a response from the file.
        try:
            with open(file) as access_file:

                items = access_file.readlines()
		response = random.choice(items)
        except:
            panic("Error", "Can't access access_keys.txt")

	print("{0}, sending reply.".format(self.api.me().name))

        # Tweet back to the user.
        self.api.update_status("@{0} {1}".format(
		status.user.screen_name.encode("utf-8"),
		response), in_reply_to_status_id=status.id)
