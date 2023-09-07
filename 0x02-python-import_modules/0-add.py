#!/usr/bin/python3

if __name__ == "__main__":
    from add_0 import add  # Import the 'add' function from 'add_0'

    a = 1
    b = 2
    result = add(a, b)  # Call the 'add' function
    print("{} + {} = {}".format(a, b, result))
