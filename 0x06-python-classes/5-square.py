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

    def area(self):
        return self.__size * self.__size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) == int:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
        else:
            raise TypeError("size must be an integer")

    def my_print(self):
        if self.__size == 0:
            print()
        for i in range(self.__size):
            print('#' * self.__size)
