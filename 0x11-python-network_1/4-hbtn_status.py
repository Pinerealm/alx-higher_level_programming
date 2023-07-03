#!/usr/bin/python3
"""Fetches the page,'https://alx-intranet.hbtn.io/status' via the
requests package and displays the response body.
"""
import requests


if __name__ == '__main__':
    res = requests.get('https://alx-intranet.hbtn.io/status')
    print('Body response:')
    print('\t- type: {}'.format(type(res.text)))
    print('\t- content: {}'.format(res.text))
