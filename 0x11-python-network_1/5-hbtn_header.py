#!/usr/bin/python3
""" Module - 3-error_code"""

if __name__ == "__main__":
    import requests
    from sys import argv

    r = requests.get(argv[1])
    print(r.headers.get("x-request-id"))
