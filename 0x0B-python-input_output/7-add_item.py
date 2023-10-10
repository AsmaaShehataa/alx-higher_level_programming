#!/usr/bin/python3
""" script that adds all arguments to a Python list"""

import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

args = list(sys.argv[1:])

try:
    O_data = load_from_json_file('add_item.json')
except Exception:
    O_data = []

O_data.extend(args)
save_to_json_file(O_data, 'add_item.json')
