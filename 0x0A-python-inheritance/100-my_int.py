#!/usr/bin/python3


class MyInt(int):

    def __eq__(self, other):  # For x == y
        if isinstance(other, int):
            if int(self) == int(other):
                return False
            else:
                return True
        return False

    def __ne__(self, other):  # For x != y OR x <> y
        if isinstance(other, int):
            if int(self) != int(other):
                return False
            else:
                return True
        return False
