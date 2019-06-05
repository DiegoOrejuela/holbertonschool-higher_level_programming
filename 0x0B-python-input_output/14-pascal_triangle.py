#!/usr/bin/python3


def pascal_triangle(n):

    matrix = []

    if n <= 0:
        return matrix

    counter = 0
    for i in range(n):
        counter += 1
        list_in = []
        for j in range(counter):
            if j == 0 or j == counter - 1:
                list_in.append(1)
            else:
                k = j - 1
                list_in.append(matrix[i - 1][k] + matrix[i - 1][j])
        matrix.append(list_in)
    return matrix
