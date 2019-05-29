#!/usr/bin/python3
def magic_string(num=[0]):
    num[0] += 1
    return("Holberton, " * (num[0] - 1) + "Holberton")
