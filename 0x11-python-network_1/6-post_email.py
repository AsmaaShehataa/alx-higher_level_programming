#!/usr/bin/python3
""" URL and an email address, sends a POST request to the passed URL"""

if __name__ == '__main__':
  from sys import argv
  import requests

  url = argv[1]
  email = argv[2]

  my_params = {'email': email}
  my_result = requests.post(url, my_params)
  print(my_result.text)
