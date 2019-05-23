#!/usr/bin/python3


class Square:
    """ Create to type of square"""
    def __init__(self, size=0, position=(0, 0)):
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

        self.my_str = "position must be a tuple of 2 positive integers"
        if type(position) != tuple:
            raise TypeError(self.my_str)
        if len(position) != 2:
            raise TypeError(self.my_str)

        self.p0 = position[0]
        self.p1 = position[1]

        if type(self.p0) == int and type(self.p1) == int:
            if self.p0 >= 0 and self.p1 >= 0:
                self.__position = position
            else:
                raise TypeError(self.my_str)
        else:
            raise TypeError(self.my_str)

    def area(self):
        return self.__size * self.__size

    @property
    def position(self):
        return self.__position

    @property
    def size(self):
        return self.__size

    @position.setter
    def position(self, value):

        if type(position) != tuple:
            raise TypeError(self.my_str)
        if len(position) != 2:
            raise TypeError(self.my_str)

        self.p0 = value[0]
        self.p1 = value[1]

        if type(self.p0) == int and type(self.p1) == int:
            if self.p0 >= 0 and self.p1 >= 0:
                self.__position = position
            else:
                raise TypeError(self.my_str)
        else:
            raise TypeError(self.my_str)

    @size.setter
    def size(self, value):
        if type(value) == int:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
        else:
            raise TypeError("size must be an integer")

    def __str__(self):
        return self.my_print()

    def my_print(self):
        self.my_list = []
        self.my_string = ""
        if self.__size == 0:
            return ''
        else:
            for i in range(self.position[1]):
                self.my_list.append('\n')
            for i in range(self.__size):
                self.my_list.append(' ' * self.position[0])
                self.my_list.append('#' * self.__size)
                if i != self.__size - 1:
                    self.my_list.append('\n')
            return self.my_string.join(self.my_list)
