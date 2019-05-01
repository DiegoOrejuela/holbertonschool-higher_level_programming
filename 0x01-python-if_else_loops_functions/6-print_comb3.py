#!/usr/bin/python3
for i in range(8):
    for j in range (1, 10):
        if i != j and i < j:
            print("{0}{1}, ".format(i, j), end="")
print("{}".format(89))
