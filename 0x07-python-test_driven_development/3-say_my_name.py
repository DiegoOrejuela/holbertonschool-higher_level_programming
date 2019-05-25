#!/usr/bin/python3
""" module that prints your name
"""


def say_my_name(first_name, last_name=""):
    """function that say my name
       My name is <first name> <last name>
    Args:
       first_name (str): mandatory
       last_name (str): opcional
    """

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is " + first_name + " " + last_name)
