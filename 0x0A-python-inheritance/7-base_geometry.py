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
