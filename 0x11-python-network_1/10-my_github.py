#!/usr/bin/python3
'''
Takes your Github credentials (username and password) and uses
the Github API to display your id
'''

import requests
import sys

if __name__ == "__main__":
    url = 'https://api.github.com/user'
    username = 'AsmaaShehataa'
    username = sys.argv[1]
    token = sys.argv[2]
    headers = {'Authorization': 'token {}'.format(token)}
    res = requests.get(url, headers=headers)
    print(res.json().get('id'))
