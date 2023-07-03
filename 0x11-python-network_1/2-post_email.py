#!/usr/bin/python3
"""Takes in a URL and an email, sends a POST request to the
passed URL with the email as a parameter, and displays the response body
"""
import urllib.request as urlreq
import urllib.parse as urlparse
import sys


if __name__ == '__main__':
    url = sys.argv[1]
    value = {'email': sys.argv[2]}
    data = urlparse.urlencode(value).encode('ascii')

    with urlreq.urlopen(url, data) as response:
        print(response.read().decode('utf-8'))
