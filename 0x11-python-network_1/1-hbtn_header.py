#!/usr/bin/python3
"""ID Request from a URL"""

if __name__ == '__main__':
  from urllib import request
  from sys import argv

  url = argv[1]
  with request.urlopen(url) as response:
    req_ID = response.getheader('X-Rewuest-Id')
    print(req_ID)
