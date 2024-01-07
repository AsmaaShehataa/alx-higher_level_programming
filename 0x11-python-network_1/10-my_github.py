#!/usr/bin/python3
"""Python script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id"""
import requests
from sys import argv
from requests.auth import HTTPBasicAuth
if __name__ == "__main__":
    url = 'https://api.github.com/user'
    user = "AsmaaShehataa"
    user = argv[1]
    passwd = argv[2]
    headers = {'Authorization': 'passwd {}'.format(passwd)}
    resp = requests.get(url, headers=headers)
    print(resp.json().get('id'))
