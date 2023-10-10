#!/usr/bin/python3
"""Append a string"""


def append_write(filename="", text=""):
    """Module to append a string at the end of text file"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
