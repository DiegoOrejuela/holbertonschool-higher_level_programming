#!/usr/bin/python3
"""Module base | Almost a circle
This module is part of repository for review everything about Python:
Import, Exceptions, Class, Private attribute, Getter/Setter, Class method,
Static method, Inheritance, Unittest, Read/Write file"""
from json import dumps, loads
from os import path
from csv import DictWriter, DictReader


class Base:
    """This class will be the “base” of all other classes in this project.
    The goal of it is to manage id attribute in all your future classes and
    to avoid duplicating the same code (by extension, same bugs)
    Attributes:
    - Class: __nb_objects.
    Methods: __init__."""

    __nb_objects = 0

    def __init__(self, id=None):
        """__init__ - method constructor.
        Args:
            id: id of object.
        Return: nothing.
        """
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """save_to_file_csv - writes the Csv string representation of list_objs
        to a file:
        Args:
            list_objs (objects)
        Return: nothing
        """
        json_file = cls.__name__ + ".csv"
        with open(json_file, mode='w', encoding="UTF-8") as f:
            list_dict = []
            for objs in list_objs:
                list_dict.append(objs.to_dictionary())
            keys = list_dict[0].keys()
            obj_writer = DictWriter(f, keys)
            obj_writer.writeheader()
            for item in list_dict:
                obj_writer.writerow(item)

    @classmethod
    def load_from_file_csv(cls):
        """load_from_file_csv - file to instances
        Args: nothing.
        Return: returns a list of instances.
        """
        json_file = cls.__name__ + ".csv"
        list_return = []
        if not path.exists(json_file):
            return list_return
        with open(json_file, mode="r", encoding="UTF-8") as f:
            obj_reader = DictReader(f)
            for row in obj_reader:
                for item in row:
                    row[item] = int(row[item])
                list_return.append(cls.create(**row))
        return list_return

    @classmethod
    def load_from_file(cls):
        """load_from_file - file to instances
        Args: nothing.
        Return: returns a list of instances.
        """
        json_file = cls.__name__ + ".json"
        list_return = []
        if not path.exists(json_file):
            return list_return
        with open(json_file, mode="r", encoding="UTF-8") as f:
            for item_list in cls.from_json_string(f.read()):
                list_return.append(cls.create(**item_list))
            return list_return

    @classmethod
    def create(cls, **dictionary):
        """create - returns an instance with all attributes already set.
        Args:
            dictionary (dict) : can be thought of as a double pointer to a
            dictionary
        Return: returns an instance with all attributes already set.
        """
        if cls.__name__ == "Rectangle":
            obj = cls(1, 1)
        if cls.__name__ == "Square":
            obj = cls(1)
        obj.update(**dictionary)
        return obj

    @staticmethod
    def from_json_string(json_string):
        """from_json_string - that returns the list of the JSON string
        representation json_string.
        Args:
            json_string (str): returns the JSON string representation.
        Return: returns the JSON string representation, Otherwise, return
        the list represented by json_string
        """
        return_list = []
        if not json_string or len(json_string) == 0:
            return return_list
        return loads(json_string)

    @staticmethod
    def to_json_string(list_dictionaries):
        """to_json_string - returns the JSON string representation
        Args:
            list_dictionaries(list)
        Return: If list_dictionaries is None or empty, return the string: "[]"
        Otherwise, return the JSON string representation of list_dictionaries
        """
        if not list_dictionaries or len(list_dictionaries) == 0:
            return "[]"
        return dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """save_to_file - writes the JSON string representation of list_objs
        to a file:
        Args:
            list_objs (objects)
        Return: nothing
        """
        json_file = cls.__name__ + ".json"
        with open(json_file, mode='w', encoding="UTF-8") as f:
            if not list_objs:
                f.write(cls.to_json_string([]))
            else:
                list_dict = []
                for objs in list_objs:
                    list_dict.append(objs.to_dictionary())

                str_list = cls.to_json_string(list_dict)
                f.write(str_list)
