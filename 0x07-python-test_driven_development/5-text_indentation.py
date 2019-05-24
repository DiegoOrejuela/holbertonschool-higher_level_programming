#!/usr/bin/python3
"""Module 5-text_indentation.py | Test-driven development Package

What you should learn from this project:
- What’s an interactive test and why tests are important
- How to write Docstrings to create tests and he basic option flags"""


def text_indentation(text):
    """text_indentation - prints a text with 2 new lines after of : ., ? and :
    Arguments: text must be a string.
    Return:Nothing"""

    if type(text) != str:
        raise TypeError("text must be a string")

    for i in range(len(text)):
        if text[i] == " ":
            j = i - 1
            if text[j] != "." and text[j] != "?" and text[j] != ":":
                print("{}".format(text[i]), end="")
        else:
            print("{}".format(text[i]), end="")
            if text[i] == "." or text[i] == "?" or text[i] == ":":
                print('\n')
