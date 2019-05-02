#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    len_argv = len(argv) - 1
    point = ":"
    plural = "s"
    if len_argv == 0:
        point = "."
    if len_argv == 1:
        plural = ""
    print("{} argument{}{}".format(len_argv, plural, point))
    for i in range(1, len(argv)):
        print("{}: {}".format(i, argv[i]))
