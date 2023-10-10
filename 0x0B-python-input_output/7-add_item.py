#!/usr/bin/python3
""" script that adds all arguments to a Python list"""

import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

args = list(sys.argv[1:])

try:
    O-data = load_from_json_file('add_item.json')
except Exception:
    O-data = []

O-data.extend(arglist)
save_to_json_file(O-data, 'add_item.json')
