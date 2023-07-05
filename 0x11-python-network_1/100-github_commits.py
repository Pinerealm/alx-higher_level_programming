#!/usr/bin/python3
"""List 10 commits (from the most recent to oldest) of the repository
“rails” by the user “rails” from the GitHub API.
"""
import requests
import sys


if __name__ == '__main__':
    owner = sys.argv[2]
    repo = sys.argv[1]
    url = 'https://api.github.com/repos/{}/{}/commits'.format(owner, repo)
    r = requests.get(url)

    try:
        json = r.json()
        for i in range(10):
            print('{}: {}'.format(json[i].get('sha'),
                                  json[i].get('commit').get('author')
                                         .get('name')))
    except ValueError:
        print('Not a valid JSON')
