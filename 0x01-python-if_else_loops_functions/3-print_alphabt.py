#!/usr/bin/python3
for char in range(ord('a'), ord('z') + 1):
    if chr(char) is not 'q' and chr(char) is not 'e':
        print("{:c}".format(char), end="")
