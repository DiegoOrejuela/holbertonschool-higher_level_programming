#!/usr/bin/python3


class BaseGeometry:
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) == int:
            if value <= 0:
                raise ValueError(name + " must be greater than 0")
        else:
            raise TypeError(name + " must be an integer")


class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)


class Square(Rectangle):
    def __init__(self, size):
        super().__init__(size, size)
        self.__size = size
