#!/usr/bin/python3

def add_integer(a, b=98):
    n = [a, b]
    n_str = ['a', 'b']
    for i in range(2):
        if type(n[i]) == float and type(n[i]) != int:
            n[i] = int(n[i])
        elif type(n[i]) != int:
            raise TypeError(n_str[i] + " must be an integer")
    return n[0] + n[1]
