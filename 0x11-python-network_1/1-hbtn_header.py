#!/usr/bin/python3
"""Python script that takes in a URL, sends a request to the URL and 
    displays the value of the X-Request-Id variable found in the 
    header of the response

Usage: ./1-hbtn_header.py <my_url>
"""
import sys
import urllib.request


if __name__ == "__main__":
    my_url = sys.argv[1]

    the_request = urllib.request.Request(my_url)
    with urllib.request.urlopen(the_request) as response:
        print(dict(response.headers).get("X-Request-Id"))
