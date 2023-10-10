#!/usr/bin/python3
"""Reading text file"""


def read_file(filename=""):
  """Print the content of the file"""
  with read_file(filename, encoding='utf-8') as f:
    print(f.read(), end="")