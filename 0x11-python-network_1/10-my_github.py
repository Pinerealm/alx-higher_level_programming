#!/usr/bin/python3
"""Displays the Github ID of a given user.
"""
import requests
import sys


if __name__ == '__main__':
    url = 'https://api.github.com/user'
    r = requests.get(url, auth=(sys.argv[1], sys.argv[2]))
    try:
        json = r.json()
        print(json.get('id'))
    except requests.exceptions.JSONDecodeError:
        print('Not a valid JSON')
