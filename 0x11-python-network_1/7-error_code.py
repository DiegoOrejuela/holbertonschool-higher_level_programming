#!/usr/bin/python3
""" Module - hbtn_header"""

if __name__ == "__main__":
    import requests
    from sys import argv

    try:
        r = requests.get(argv[1])
        r.raise_for_status()
        print(r.text)

    except:
        print("Error code: {}".format(r.status_code))
