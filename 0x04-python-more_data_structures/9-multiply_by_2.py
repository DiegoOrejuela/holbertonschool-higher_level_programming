#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    dictionary = a_dictionary.copy()
    for i in dictionary:
        dictionary[i] = dictionary[i] * 2
    return dictionary
