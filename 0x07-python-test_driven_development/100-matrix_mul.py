#!/usr/bin/python3
"""Module matrix_divided.py | Test-driven development Package

What you should learn from this project:
- What’s an interactive test and why tests are important
- How to write Docstrings to create tests and he basic option flags"""


def matrix_mul(m_a, m_b):
    """ matrix_divided - divides all elements of a matrix.
    Arguments: matrix must be a list of lists of integers or floats.
    Return: new matrix with value divided"""

    if len(m_a[0]) != len(m_b):
        raise ValueError(""

    for row_a in range(len(m_a)):  #filas m_a
        #for num_a in range(len(m_a[row_a])): #nums m_a (col)
        list_in = []
        for i in range(len(m_b[0])): #len_col m_b
            result = 0
            for row_b in range(len(m_b)): #nums_b (filas)
                result += m_a[row_a][row_b] * m_b[row_b][i]
            list_in.append(result)
        new_matrix.append(list_in)

    return new_matrix
