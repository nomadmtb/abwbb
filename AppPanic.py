#!/usr/bin/python
# AppPanic.py: Use this function when gracefully exiting the application.


def panic(error_type, message):

    if error_type != "" and message != "":
        print("{0}: {1}".format(error_type, message))
    else:
        print("Please provide a valid error")

    exit(1)
