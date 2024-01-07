#!/usr/bin/python3
"""Python script that takes in a letter and sends a POST request"""
import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) == 2:
        q = argv[1]
    else:
        q = ""
    resp = requests.post('http://0.0.0.0:5000/search_user')
    try:
        resp.raise_for_status()
        if resp.json():
            print("[{}] {}".format(resp.json().get('id'),
                                   resp.json().get('name')))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
    except requests.exceptions.HTTPError as err:
        print("Error code: {}".format(resp.status_code))
