#!/usr/bin/python3
"""Write a Python script that takes in a URL, sends a request to the URL and displays the body of the response.

Usage: ./7-error_code.py <URL>
  - Handles HTTP errors.
"""
import sys
import requests


if __name__ == "__main__":
    myurl = sys.argv[1]

    results = requests.get(umyurlrl)
    if results.status_code >= 400:
        print("Error code: {}".format(results.status_code))
    else:
        print(results.text)
