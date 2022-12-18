#!/usr/bin/python3
"""This script sends a request to a URL and displays the value of the
X-Request-Id variable found in the response header."""
import requests
import sys


if __name__ == '__main__':
    r = requests.get(sys.argv[1])
    print(r.headers.get('X-Request-Id'))
