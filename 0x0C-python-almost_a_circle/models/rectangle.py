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

    def __str__(self):
        """__str__ - Create a new string object from the given object.
        Args: nothing
        return: empty string
        """
        return "[{}] ({}) {}/{} - {}/{}".format(self.__class__.__name__,
                                              self.id, self.x, self.y,
                                              self.width, self.height)

    def display(self):
        """display - prints in stdout the Rectangle instance with the
        character #
        Args: none
        return: nothing
        """
        for i in range(self.__height):
            print(self.__width * '#')

    def area(self):
        """area - width * height.
        Args: nothing
        Return: area of rectangle.
        """
        return self.__width * self.__height

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
        if type(value) != int:
            raise TypeError("width must be an integer")
        else:
            if value <= 0:
                raise ValueError("width must be > 0")
            self.__width = value

    @height.setter
    def height(self, value):
        """height - set height.
        Args:
        - value (int): set height of rectangle.
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        else:
            if value <= 0:
                raise ValueError("height must be > 0")
            self.__height = value

    @x.setter
    def x(self, value):
        """height - set x of rectangle.
        Args:
        - value (int): set x of rectangle.
        """
        if type(value) != int:
            raise TypeError("x must be an integer")
        else:
            if value < 0:
                raise ValueError("x must be >= 0")
            self.__x = value

    @y.setter
    def y(self, value):
        """height - set y of rectangle
        Args:
        - value (int): set y of rectangle.
        """
        if type(value) != int:
            raise TypeError("y must be an integer")
        else:
            if value < 0:
                raise ValueError("y must be >= 0")
            self.__y = value
