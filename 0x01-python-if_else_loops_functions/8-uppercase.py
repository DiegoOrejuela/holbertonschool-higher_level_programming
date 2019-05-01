#!/usr/bin/python3
def uppercase(str):
    for i in str:
        upper = ord(i)
        if ord(i) >= ord('a') and ord(i) <= ord('z'):
            upper = ord(i) - 32
        print("{}".format(chr(upper)), end="")
    print()
