#!/usr/bin/python3
"""Module 0-add_integer-py | Test-driven development Package

What you should learn from this project:
- What’s an interactive test and why tests are important
- How to write Docstrings to create tests and he basic option flags"""


def add_integer(a, b=98):
    """add_integer - adds 2 integers.
    Arguments: a and b must be integers or floats
    Return:the addition of a and b"""

    n = [a, b]
    n_str = ['a', 'b']
    for i in range(2):
        if i == None or type(n[i]) != int and type(n[i]) != float:
            raise TypeError(n_str[i] + " must be an integer")
    return int(n[0]) + int(n[1])
