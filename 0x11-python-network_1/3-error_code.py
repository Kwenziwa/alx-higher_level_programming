#!/usr/bin/python3
"""sends a request to the URL and displays the body of the response.

Usage: ./3-error_code.py <URL>
  - Handles HTTP errors.
"""
import sys
import urllib.error
import urllib.request


if __name__ == "__main__":
    the_url = sys.argv[1]

    the_request = urllib.request.Request(the_url)
    try:
        with urllib.request.urlopen(the_request) as results:
            print(results.read().decode("ascii"))
    except urllib.error.HTTPError as error_msg:
        print("Error code: {}".format(error_msg.code))
