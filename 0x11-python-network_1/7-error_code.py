#!/usr/bin/python3
"""
    Script that takes in a URL, sends a request to
    the URL and displays the body of the response
"""
import requests
import sys


req = requests.get(sys.argv[1])
if req.status_code >= 400:
    print(f"Error code: {req.status_code}")
else:
    print(req.text)
