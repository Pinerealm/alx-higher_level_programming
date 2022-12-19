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
    url = 'http://0.0.0.0:5000/search_user'
    r = requests.post(url, data={'q': q})

    try:
        data = r.json()
        if data:
            print('[{}] {}'.format(data.get('id'), data.get('name')))
        else:
            print('No result')
    except requests.exceptions.JSONDecodeError:
        print('Not a valid JSON')
