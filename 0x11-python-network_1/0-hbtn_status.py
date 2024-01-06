#!/usr/bin/python3
"""
Python script that fetches https://alx-intranet.hbtn.io/status
"""

from urllib import request
myurl = 'https://alx-intranet.hbtn.io/status'
with request.urlopen(myurl) as response:
    my_page = response.read()
    print('Body response:')
    print('\t- type: {}'.format(type(my_page)))
    print('\t- content: {}'.format(my_page))
    print('\t- utf8 content: {}'.format(my_page.decode('utf-8')))
