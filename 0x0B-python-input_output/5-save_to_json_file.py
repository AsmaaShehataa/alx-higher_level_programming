#!/usr/bin/python3
"""Function save to json file"""
import json


def save_to_json_file(my_obj, filename):
    """write object to a text using json"""
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(my_obj, file)
