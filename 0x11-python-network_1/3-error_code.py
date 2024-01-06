#!/usr/bin/python3
""" script to that takes in a URL, sends a response"""

if __name__ == '__main__':
    from urllib import request, error
    from sys import argv

    url = argv[1]

    try:
        with request.urlopen(url) as response:
            body = response.read().decode('utf-8')
            print(body)

    except error.HTTPError as exception:
        print(f"Error code: {exception.code}")
