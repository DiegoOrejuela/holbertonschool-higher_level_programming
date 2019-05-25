#!/usr/bin/python3
"""Module matrix_mul.py | Test-driven development Package

What you should learn from this project:
- What’s an interactive test and why tests are important
- How to write Docstrings to create tests and he basic option flags"""


def matrix_mul(m_a, m_b):
    """ matrix_mul - multiplies 2 matrices.
    Arguments: 2 matrices.
    Return: new matrix multiplied"""

    matrix_s = [m_a, m_b]
    m_s = ["m_a", "m_b"]
    # Matrix_mul don't is list
    for i in range(len(matrix_s)):
        if type(matrix_s[i]) != list:
            raise TypeError(m_s[i] + " must be a list")

    # Matrix doesn't list of list
    for i in range(len(matrix_s)):
        for j in range(len(matrix_s[i])):
            if type(matrix_s[i][j]) != list:
                raise TypeError(m_s[i] + " must be a list of lists")
    # Empty matrix
    for i in range(len(matrix_s)):
        if len(matrix_s[i]) == 0:
            raise TypeError(m_s[i] + " can't be empty")
        elif len(matrix_s[i]) == 1:
            if len(matrix_s[i][0]) == 0:
                raise TypeError(m_s[i] + " can't be empty")

    # Integer o floats
    err = " should contain only integers or floats"
    for h in range(len(matrix_s)):
        for i in range(len(matrix_s[h])):
            for j in range(len(matrix_s[h][i])):
                if type(matrix_s[h][i][j]) != float\
                   and type(matrix_s[h][i][j]) != int:
                    raise TypeError(m_s[h] + err)
    # Rect list
    err = " must should be of the same size"
    for i in range(len(matrix_s)):
        for j in range(len(matrix_s[i])):
            if len(matrix_s[i][0]) != len(matrix_s[i][j]):
                raise TypeError("each row of " + m_s[i] + err)

    # Don't multiple
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # Operation
    new_matrix = []
    for row_a in range(len(m_a)):  # Filas m_a
        # For num_a in range(len(m_a[row_a])): # Nums m_a (col)
        list_in = []
        for i in range(len(m_b[0])):  # Len_col m_b
            result = 0
            for row_b in range(len(m_b)):  # Nums_b (filas)
                result += m_a[row_a][row_b] * m_b[row_b][i]
            list_in.append(result)
        new_matrix.append(list_in)

    return new_matrix
