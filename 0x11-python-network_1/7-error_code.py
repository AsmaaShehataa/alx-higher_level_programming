#!/usr/bin/python3
"""Python script that takes in a URL, sends a request to the URL"""

from sys import argv
import requests

if __name__ == "__main__":
    try:
        response = requests.get(argv[1])
        error = response.raise_for_status()
        if not error:
            print(response.text)
    except requests.exceptions.HTTPError as err:
        if response.status_code >= 400:
            print(f'Error code: {response.status_code}')
