#!/usr/bin/python3
"""Write a Python script that takes in a URL and an email address, sends a POST request to the passed URL with the email as a parameter, and finally displays the body of the response.

Usage: ./6-post_email.py <URL> <email>
  - Displays the body of the response.
"""
import sys
import requests


if __name__ == "__main__":
    myurl = sys.argv[1]
    myv = {"email": sys.argv[2]}

    results = requests.post(myurl, data=myv)
    print(results.text)
