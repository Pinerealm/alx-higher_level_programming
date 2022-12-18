#!/usr/bin/python3
"""This script takes in a letter as a parameter and sends a POST request to
'http://0.0.0.0:5000/search_user'"""
import requests
import sys


if __name__ == '__main__':
    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""
    url = 'http://689d9351c613.8f0453a5.alx-cod.online:5000/search_user'
    r = requests.post(url, data={'q': q})
    try:
        json = r.json()
        if json:
            print('[{}] {}'.format(json.get('id'), json.get('name')))
        else:
            print('No result')
    except ValueError:
        print('Not a valid JSON')
