#!/usr/bin/python3
""" Module - 3-error_code"""

if __name__ == "__main__":
    import urllib.request
    from sys import argv

    try:
        with urllib.request.urlopen(argv[1]) as response:
            print(response.read().decode())

    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
