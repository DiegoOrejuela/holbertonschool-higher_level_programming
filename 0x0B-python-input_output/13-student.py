#!/usr/bin/python3


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if type(attrs) == list:
            for item in attrs:
                if type(item) != str:
                    return self.__dict__
            new_dict = {}
            for key in self.__dict__:
                for item in attrs:
                    if key == item:
                        new_dict[key] = self.__dict__[key]
            return new_dict
        else:
            return self.__dict__

    def reload_from_json(self, json):
        self.__dict__ = json
