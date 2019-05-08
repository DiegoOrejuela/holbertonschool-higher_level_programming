#!/usr/bin/python3
def divisible_by_2(my_list=[]):

    if(len(my_list) == 0):
        return(None)

    list_return = []

    for num in my_list:
        if num % 2 == 0:
            list_return.append(True)
        else:
            list_return.append(False)
    return(list_return)
