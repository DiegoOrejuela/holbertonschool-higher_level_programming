#!/usr/bin/python3


def append_after(filename="", search_string="", new_string=""):

    new_text = ""

    with open(filename, encoding="UTF-8") as f:
        for line in f:
            new_text += str(line)
            if line.find(search_string) != -1:
                new_text += new_string

    with open(filename, mode='w', encoding="UTF-8") as f:
        f.write(new_text)
