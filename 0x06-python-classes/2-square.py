#!/usr/bin/python3


class Square:
    """ Create to type of square"""
    def __init__(self, size=0):
        """Example of docstring on the __init__ method.

        args:
            size: num of size.
        """
        if type(size) == int:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size

        else:
            raise TypeError("size must be an integer")
