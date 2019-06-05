#!/usr/bin/python3


def number_of_lines(filename=""):
    with open(filename, encoding="UTF-8") as f:
        counter = 0
        for line in f:
            counter += 1
    return counter
