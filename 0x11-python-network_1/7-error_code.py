#!/usr/bin/python3
"""Python script that takes in a URL, sends a request to the URL"""

from sys import argv
import requests

if __name__ == '__main__':
    try:
        resp = requests.get(argv[1])
        err = resp.raise_for_status()
        if not err:
            print(resp.text)
    except requests.exceptions.HTTPError as err:
        if resp.status_code >= 400:
            print(f'Error code: {resp.status_code}')
