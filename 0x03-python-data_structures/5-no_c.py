#!/usr/bin/python3
def no_c(my_string):
    my_list = []
    new_str = ""

    for i in my_string:
        my_list.append(i)

    for x in range(my_list.count("c")):
        my_list.remove("c")

    for x in range(my_list.count("C")):
        my_list.remove("C")

    for x in my_list:
        new_str += x

    return(new_str)
