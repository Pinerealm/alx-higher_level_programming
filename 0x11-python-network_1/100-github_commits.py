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
        count = 0
        json = r.json()
        for commit in json:
            print('{}: {}'.format(commit.get('sha'),
                                  commit.get('commit').get('author')
                                        .get('name')))
            count += 1
            if count == 10:
                break
    except ValueError:
        print('Not a valid JSON')
