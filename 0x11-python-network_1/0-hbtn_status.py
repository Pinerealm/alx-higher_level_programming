#!/usr/bin/python3
"""This script fetches 'https://alx-intranet.hbtn.io/status'"""
import urllib.request as urlreq


with urlreq.urlopen('https://alx-intranet.hbtn.io/status') as response:
    res = response.read()

print('Body response:')
print('\t- type: {}'.format(type(res)))
print('\t- content: {}'.format(res))
print('\t- utf8 content: {}'.format(res.decode()))
