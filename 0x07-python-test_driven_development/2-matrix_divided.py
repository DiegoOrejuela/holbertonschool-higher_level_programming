#!/usr/bin/python3
"""Module matrix_divided.py | Test-driven development Package

What you should learn from this project:
- What’s an interactive test and why tests are important
- How to write Docstrings to create tests and he basic option flags"""


def matrix_divided(matrix, div):
    """ matrix_divided - divides all elements of a matrix.
    Arguments: matrix must be a list of lists of integers or floats.
    Return: new matrix with value divided"""

    # Review div
    if type(div) == float and type(div) != int:
            n[i] = int(n[i])
    elif type(div) != int:
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")

    # Review Len List
    for row in matrix:
        if len(matrix[0]) != len(row):
            raise TypeError("Each row of the matrix must have the same size")

    # Review if number are Int/float and convert int in float
    str_err = "matrix must be a matrix (list of lists) of integers/floats"
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if type(matrix[i][j]) == float and type(matrix[i][j]) != int:
                matrix[i][j] = int(matrix[i][j])
            elif type(matrix[i][j]) != int:
                raise TypeError(str_err)
    # Div all elements of matrix
    new_matrix = []
    for i in range(len(matrix)):
        list_in = []
        for j in range(len(matrix[i])):
            list_in.append(round(matrix[i][j] / div, 2))
        new_matrix.append(list_in)

    return new_matrix
