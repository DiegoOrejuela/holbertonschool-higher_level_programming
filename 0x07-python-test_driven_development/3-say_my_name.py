#!/usr/bin/python3
"""Module 3-say_my_name.py | Test-driven development Package

What you should learn from this project:
- What’s an interactive test and why tests are important
- How to write Docstrings to create tests and he basic option flags"""


def say_my_name(first_name, last_name=""):
    """3-say_my_name - function that prints My name is <first name> <last name>.
    Arguments: first_name and last_name must be strings otherwise.
    Return:Nothing"""

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))
