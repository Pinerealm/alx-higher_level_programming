#!/usr/bin/python3
"""This script takes in a URL, sends a request to the URL and displays
the response bode (decoded in utf-8).
Also handles HTTP errors.
"""
from urllib.request import Request, urlopen
from urllib.error import HTTPError
import sys


if __name__ == '__main__':
    url = sys.argv[1]
    req = Request(url)
    try:
        with urlopen(req) as response:
            print(response.read().decode('utf-8'))
    except HTTPError as e:
        print('Error code: {}'.format(e.code))
