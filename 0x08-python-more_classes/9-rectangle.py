#!/usr/bin/python3
"""Module 8-rectangle | More Classes and Objects

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

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """__init__ - method constructor.
        Args:
            width (int): width of rectangle.
            height (int): height of rectangle
        """
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    @classmethod
    def square(cls, size=0):
        """square - method constructor.
        Args:
            size (int): value for size of square.
        """
        return cls(size, size)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """bigger_or_equal - returns the biggest rectangle based on the area.
        Args:
            rect_1 (Rectangule): first rectangle.
            rect_2 (Rectangule): second rectangle
        """
        if type(rect_1) != Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif type(rect_2) != Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() < rect_2.area():
            return rect_2
        elif rect_1.area() > rect_2.area():
            return rect_1
        else:
            return rect_1

    def __str__(self):
        """__str__ - Create a new string object from the given object.
        Args: nothing
        return: empty string
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        for i in range(self.__height):
            print(self.__width * self.print_symbol, end="")
            if i != self.__height - 1:
                print()
        return ""

    def __del__(self):
        """__del__ - delete to object Rectangule.
        Args: nothing
        return: Nothing.
        """
        Rectangle.number_of_instances -= 1
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
