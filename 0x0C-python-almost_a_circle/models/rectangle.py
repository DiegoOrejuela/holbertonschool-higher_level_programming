#!/usr/bin/python3
"""Module base | Almost a circle
This module is part of repository for review everything about Python:
Import, Exceptions, Class, Private attribute, Getter/Setter, Class method,
Static method, Inheritance, Unittest, Read/Write file"""
from models.base import Base


class Rectangle(Base):
    """Rectangle - defines a rectangle.
    Attributes: width, height, x, y
    Method:__init__, [width, height, x, y] setter and getter.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """__init__ - method constructor.
        Args:
            width (int): width of rectangle.
            height (int): height of rectangle
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """width - get width.
        Args: nothing
        """
        return self.__width

    @property
    def height(self):
        """height - get height.
        Args: nothing
        """
        return self.__height

    @property
    def x(self):
        """height - get x.
        Args: nothing
        """
        return self.__x

    @property
    def y(self):
        """height - get y.
        Args: nothing
        """
        return self.__y

    @width.setter
    def width(self, value):
        """width - set width.
        Args:
        - value (int): set width of rectangle.
        """
        self.__width = value

    @height.setter
    def height(self, value):
        """height - set height.
        Args:
        - value (int): set height of rectangle.
        """
        self.__height = value

    @x.setter
    def x(self, value):
        """height - set x of rectangle.
        Args:
        - value (int): set x of rectangle.
        """
        self.__x = value

    @y.setter
    def y(self, value):
        """height - set y of rectangle
        Args:
        - value (int): set y of rectangle.
        """
        self.__y = value
