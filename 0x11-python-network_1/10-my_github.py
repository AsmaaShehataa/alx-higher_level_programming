#!/usr/bin/python3
"""Python script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id"""

import requests
from sys import argv

if __name__ == "__main__":
    url = 'https://api.github.com/user'
    username = 'AsmaaShehataa'
    username = argv[1]
    password = argv[2]
    headers = {'Authorization': 'password {}'.format(password)}
    resp = requests.get(url, headers=headers)
    print(resp.json().get('id'))
