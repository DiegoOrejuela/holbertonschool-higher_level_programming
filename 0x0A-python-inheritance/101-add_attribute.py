#!/usr/bin/python3


def add_attribute(obj, attr, value):
    if type(attr) != str:
        raise TypeError("can't add new attribute")
    for item in dir(obj):
        if item == "__dict__":
            setattr(obj, attr, value)
            return
    raise TypeError("can't add new attribute")
