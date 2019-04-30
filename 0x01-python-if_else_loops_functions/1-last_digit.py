#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
signed = ""
if number < 0:
    signed = "-"
strnum = str(number)
lastdigit = int(strnum[-1])
if lastdigit > 5:
    stri = "and is greater than 5"
elif lastdigit == 0:
    stri = "and is 0"
else:
    stri = "and is less than 6 and not 0"

print("Last digit of {0} is {1}{2} {3}".format(number, signed, lastdigit, stri))
