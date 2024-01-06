#!/usr/bin/python3
"""Python script that takes in a URL and an email, 
sends a POST request to the passed URL
"""

if __name__ == '__name__':
  from sys import argv
  from urllib import request, parse

  url = argv[1]
  email = argv[2]

  my_prms = parse.urlencode({'email': email}).encode('utf-8') #encoding - sending - Post
  with request.urlopen(url, data=my_prms) as response:
    content = response.read().decode('utf-8') #decoding - receiving
    print(content)
