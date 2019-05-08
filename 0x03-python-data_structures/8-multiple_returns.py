#!/usr/bin/python3
def multiple_returns(sentence):

    leng = len(sentence)
    first_char = ""

    if leng == 0:
        first_char = None
    else:
        first_char = sentence[0]

    return leng, first_char
