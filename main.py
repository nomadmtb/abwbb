#!/usr/bin/python

from Twitter import Twitter


# Main Routine...
if __name__ == '__main__':

    print("---ABW Beer Bot---")

    # Create our bot instance.
    myBot = Twitter()

    # Start the monitor.
    myBot.start_monitor()
