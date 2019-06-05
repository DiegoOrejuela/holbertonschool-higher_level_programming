#!/usr/bin/python3
from json import dumps


def save_to_json_file(my_obj, filename):
    with open(filename, mode='w', encoding="UTF-8") as f:
        str_json = dumps(my_obj)
        f.write(str_json)
