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
    headers = {'Authorization': 'password {}'.format(passwd)}
    resp = requests.get(url, headers=headers)
    try:
        resp.raise_for_status()
        print(resp.json().get('id'))
    except requests.exceptions.HTTPError as err:
        print("Error code: {}".format(resp.status_code))
