#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):

    a0, a1, b0, b1 = 0, 0, 0, 0

    if len(tuple_a) == 1:
        a0 = tuple_a[0]
    elif len(tuple_a) == 2:
        a0 = tuple_a[0]
        a1 = tuple_a[1]

    if len(tuple_b) == 1:
        b0 = tuple_b[0]
    elif len(tuple_b) == 2:
        b0 = tuple_b[0]
        b1 = tuple_b[1]

    v1 = a0 + b0
    v2 = a1 + b1

    t = (v1, v2)
    return(t)
