#!/usr/bin/python3
"""This script sends a request to a URL and displays the value of the
X-Request-Id variable found in the header of the response.
"""
import urllib.request as urlreq
import sys


with urlreq.urlopen(sys.argv[1]) as response:
    print(response.headers.get('X-Request-Id'))
