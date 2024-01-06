#!/usr/bin/python3
""" send request using requests method"""

if __name__ == '__main__':
    import requests
    from sys import argv

    req = requests.get(argv[1])
    print(req.headers.get('X-Request-Id'))
