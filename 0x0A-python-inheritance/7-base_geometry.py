#!/usr/bin/python3
"""7-base_geometry | Inheritance
    What you should learn from this project:
    - What’s an interactive test and why tests are important
    - How to write Docstrings to create tests and he basic option flags"""


class BaseGeometry:
    """Base Geometry
    Methods:
    - area
    - integer_validator
    Arguments = no one"""

    def area(self):
        """ area - that raises an Exception with the message area() is not
        implemented.
        Arguments: none.
        Return: nothing"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ integer_validor - validates value.
        Arguments: name and value.
        Return: nothing"""
        if type(value) == int:
            if value <= 0:
                raise ValueError(name + " must be greater than 0")
        else:
            raise TypeError(name + " must be an integer")
