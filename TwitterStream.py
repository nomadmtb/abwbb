#!/usr/bin/python
# TwitterStream.py: This is the streaming implementation for the application.

from AppPanic import panic
import tweepy
import os


class TwitterStream(tweepy.StreamListener):

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
        self.authentication = tweepy.OAuthHandler(self.consumer, self.consumer_secret)
        self.authentication.set_access_token(self.access, self.access_secret)
        self.api = tweepy.API(self.authentication)

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

        # Play the sound.
        os.system("afplay sounds/Tune.m4a &")

        print("New @reply:")

        # Print the details.
        print("\t{0}:\t{1}\n".format(
            status.user.screen_name.encode("utf-8"),
            status.text.encode("utf-8"))
        )
