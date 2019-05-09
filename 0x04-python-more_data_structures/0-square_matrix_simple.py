#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    nmatrix = []
    for i in range(len(matrix)):
        nmatrix.append(list(map(lambda x: x * x, matrix[i])))
    return nmatrix
