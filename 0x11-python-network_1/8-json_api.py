#!/usr/bin/python3
"""This script takes in a letter and sends a POST request to a server
with the letter as a parameter. The server returns a JSON object"""
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
        if json and r.raise_for_status() is None:
            print('[{}] {}'.format(json.get('id'), json.get('name')))
        else:
            print('No result')
    except requests.exceptions.JSONDecodeError:
        print('Not a valid JSON')
