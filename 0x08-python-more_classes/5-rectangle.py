#!/usr/bin/python3
"""Module 5-rectangle | More Classes and Objects

What you should learn from this project:
- What is a class, What is an object and an instance
- What is the difference between a class and an object or instance"""


class Rectangle:
    """Rectangle - defines a rectangle.
    Attributes: nothing.
    Method:
    - __init__
    - width
    - height
    - width(value)
    - height(value)."""

    def __init__(self, width=0, height=0):
        """__init__ - method constructor.
        Args:
            width (int): width of rectangle.
            height (int): height of rectangle
        """
        self.width = width
        self.height = height

    def __str__(self):
        """__str__ - Create a new string object from the given object.
        Args: nothing
        return: empty string
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        for i in range(self.__height):
            print(self.__width * '#', end="")
            if i != self.__height - 1:
                print()
        return ""

    def __del__(self):
        """__del__ - delete to object Rectangule.
        Args: nothing
        return: Nothing.
        """
        print("Bye rectangle...")

    def __repr__(self):
        """__repr__ - Return the canonical string representation of the object
        Args: nothing
        return: empty string
        """
        return "Rectangle(" + str(self.__width) + ",\
 " + str(self.__height) + ")"

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

    def area(self):
        """area - width * height.
        Args: nothing
        Return: area of rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """perimeter - width * 2 + height * 2.
        Args: nothing
        Return: perimeter of rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return self.__width * 2 + 2 * self.__height

    @width.setter
    def width(self, value):
        """width - set width.
        Args:
        - value (int): set width of rectangle.
        """
        if type(value) == int:
            if value < 0:
                raise ValueError("width must be >= 0")
            else:
                self.__width = value

        else:
            raise TypeError("width must be an integer")

    @height.setter
    def height(self, value):
        """height - set height.
        Args:
        - value (int): set height of rectangle.
        """

        if type(value) == int:
            if value < 0:
                raise ValueError("height must be >= 0")
            else:
                self.__height = value

        else:
            raise TypeError("height must be an integer")
