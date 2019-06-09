#!/usr/bin/python3
"""Module base | Almost a circle
This module is part of repository for review everything about Python:
Import, Exceptions, Class, Private attribute, Getter/Setter, Class method,
Static method, Inheritance, Unittest, Read/Write file"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square - defines a square.
    Attributes: inheritance by Rectangle.
    Methods:__init__, [width, height, x, y] setter and getter.
    """
    def __init__(self, size, x=0, y=0, id=None):
        """__init__ - method constructor.
        Args:
            size (int): width of rectangle.
            x (int): position x
            y (int):  position y
            id (int): id square
        """
        super().__init__(size, size, x, y, id)

    def to_dictionary(self):
        """to_dictionary - returns the dictionary representation of a Rectangle.
        Args: nothing
        return: the dictionary representation of a Rectangle.
        """
        rep_dict = super().to_dictionary()
        rep_dict["size"] = rep_dict.pop("width")
        rep_dict.pop("height")
        return rep_dict

    def update(self, *args, **kwargs):
        """update - Update the class Rectangle, that assigns an argument to
        each attribute:
        Args:
            *args (list):
                1st argument should be the id attribute
                2nd argument should be the width attribute
                3rd argument should be the height attribute
                4th argument should be the x attribute
                5th argument should be the y attribute
            **kwargs(dict):
                 key/value (keyworded arguments)
        """
        if len(args) >= 2:
            args = list(args)
            args.insert(2, args[1])
        temp_kwargs = kwargs.copy()
        for key in temp_kwargs:
            if key == "size":
                kwargs["width"] = kwargs[key]
                kwargs["height"] = kwargs[key]

        super().update(*args, **kwargs)

    @property
    def size(self):
        """size - get size.
        Args: nothing
        """
        return super().width

    @size.setter
    def size(self, value):
        """size - set size.
        Args:
        - value (int): set width and height of rectangle.
        """
        self.width = value
        self.height = value

    def __str__(self):
        """__str__ - Create a new string object from the given object.
        Args: nothing
        return: empty string
        """
        return "[{}] ({}) {}/{} - {}".format(self.__class__.__name__,
                                             self.id, self.x, self.y,
                                             self.height)
