#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list is not None:
        num_max = 0

        for num in my_list:
            if num > num_max:
                num_max = num
        return(num_max)
