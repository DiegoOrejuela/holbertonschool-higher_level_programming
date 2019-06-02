#!/usr/bin/python3
"""Module 4-print_square.py | Test-driven development Package

What you should learn from this project:
- What’s an interactive test and why tests are important
- How to write Docstrings to create tests and he basic option flags"""


def print_square(size):
    """4-print_square - prints a square with the character #.
    Arguments: size is the size length of the square.
    Return:Nothing"""

    if type(size) == int:
            if size < 0:
                raise ValueError("size must be >= 0")
    else:
        raise TypeError("size must be an integer")

    if size == 0:
        return
    else:
        for i in range(size):
            print('#' * size)
