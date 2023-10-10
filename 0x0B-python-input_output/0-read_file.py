#!/usr/bin/python3
"""Reading text file"""


def read_file(filename=""):
	"""Print the content of the file"""
	with read_file("my_file_0.txt", encoding="utf-8") as file:
		print(file.read(), end="")
