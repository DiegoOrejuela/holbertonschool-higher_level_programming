#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return(0)
    number1, number2 = 0, 0
    for i in my_list:
        number1 += i[0] * i[1]
        number2 += i[1]
    result = number1 / number2
    return result
