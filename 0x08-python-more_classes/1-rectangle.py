#!/usr/bin/python3
"""Module 0-rectangle | More Classes and Objects

What you should learn from this project:
- What is a class, What is an object and an instance
- What is the difference between a class and an object or instance"""


class Rectangle:
    """Rectangle - defines a rectangle.
    Attributes: nothing.
    Method: nothing."""

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @width.setter
    def width(self, value):
        if type(value) == int:
            if value < 0:
                raise ValueError("width must be >= 0")
            else:
                self.__width = value

        else:
            raise TypeError("width must be an integer")

    @height.setter
    def height(self, value):

        if type(value) == int:
            if value < 0:
                raise ValueError("height must be >= 0")
            else:
                self.__height = value

        else:
            raise TypeError("height must be an integer")
