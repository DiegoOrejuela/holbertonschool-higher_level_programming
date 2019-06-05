#!/usr/bin/python3


def number_of_lines(filename=""):
    with open(filename, encoding="UTF-8") as f:
        counter = 0
        for line in f:
            counter += 1
    return counter


def read_lines(filename="", nb_lines=0):
    with open(filename, encoding="UTF-8") as f:
        num_lin = number_of_lines(filename)
        if nb_lines <= 0 or nb_lines >= num_lin:
            print(f.read(), end="")
        else:
            for i in range(nb_lines):
                print(f.readline(), end="")
