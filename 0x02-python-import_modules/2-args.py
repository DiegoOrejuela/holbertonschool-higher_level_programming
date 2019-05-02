#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    len_argv = len(argv) - 1
    print("{} argument{}{}".format(len_argv, "s" if len_argv != 1 else "",
                                 "." if len_argv == 0 else ":"))
    for i in range(1, len(argv)):
        print("{}: {}".format(i, argv[i]))
