#!/usr/bin/python3
"""This script fetches 'https://intranet.hbtn.io/status'
via the package, requests"""
import requests


if __name__ == '__main__':
    r = requests.get('https://intranet.hbtn.io/status')
    print('Body response:')
    print('\t- type: {}'.format(type(r.text)))
    print('\t- content: {}'.format(r.text))
