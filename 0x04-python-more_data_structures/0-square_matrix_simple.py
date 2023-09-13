#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    copied_matrix = matrix.copy()

    for i in range(len(matrix)):
        copied_matrix[i] = list(map(lambda x: x**2, matrix[i]))

    return (copied_matrix)
