#!/usr/bin/python

from Twitter import Twitter
from TwitterStream import TwitterStream


# Main Routine...
if __name__ == '__main__':

    print("\n   d[-_-]b  ")
    print("---BeerBot---\n")

    myBot = TwitterStream()
    myBot.start_stream()
