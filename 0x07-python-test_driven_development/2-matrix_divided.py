#!/usr/bin/python3
"""
Matrix Division
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a square matrix by the given divisor.
    """
    list_err = 'matrix must be a matrix (list of lists) of integers/floats'
    lis_size_err = 'Each row of the matrix must have the same size'

    if type(matrix) != list:
        raise TypeError(list_err)
    for item in range(len(matrix)):
        res = item - 1
        if len(matrix[item]) != len(matrix[res]):
            raise TypeError(lis_size_err)
    if isinstance(div, int) is False:
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')

    return [[round(item/div, 2) for item in l_list] for l_list in matrix]

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
