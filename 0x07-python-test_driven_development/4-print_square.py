#!/usr/bin/python3

"""printing square with the character #"""


def print_square(size):
    """
    function to print square
    """
    if isinstance(size, int) is False:
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    for i in range(0, size):
        print('#' * size)


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/4-print_square.txt")
