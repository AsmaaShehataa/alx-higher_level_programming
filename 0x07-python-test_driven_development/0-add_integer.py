#!/usr/bin/python3
"""Module for addition of two int"""


def add_integer(a, b=98):
    """Addition of two int

    Args:
        a: 1st int
        b: 2nd int, set defualt 98

    Raises:
        Type error: if a, b are not int, float.

    Return:
        The sum of integers
    """

    if isinstance(a, (int, float)) is False:
        raise TypeError("a must be integer")
    if isinstance(b, (int, float)) is False:
        raise TypeError("b must be integer")
    return int(a) + int(b)

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
