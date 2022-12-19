#!/usr/bin/python3
"""This script takes my Github credentials (username and password) and"
uses the Github API to display my id"""
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
