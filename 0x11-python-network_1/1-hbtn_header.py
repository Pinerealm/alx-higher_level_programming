#!/usr/bin/python3
"""Sends a request to a URL and displays the value of the
X-Request-Id variable found in the header of the response.
"""
import urllib.request as urlreq
import sys


if __name__ == '__main__':
    with urlreq.urlopen(sys.argv[1]) as response:
        print(response.headers.get('X-Request-Id'))
