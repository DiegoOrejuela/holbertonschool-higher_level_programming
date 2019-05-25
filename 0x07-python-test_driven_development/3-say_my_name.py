#!/usr/bin/python3
"""Module 3-say_my_name.py | Test-driven development Package

What you should learn from this project:
- What’s an interactive test and why tests are important
- How to write Docstrings to create tests and he basic option flags"""


def say_my_name(first_name, last_name=""):
    """3-say_my_name - function that prints My name is <first name> <last name>.
    Arguments: first_name and last_name must be strings otherwise.
    Return:Nothing"""

    n = [first_name, last_name]
    n_str = ['first_name', 'last_name']

    for i in range(2):
        if type(n[i]) != str:
            raise TypeError(n_str[i] + " must be a string")
    print("My name is {} {}".format(first_name, last_name))
