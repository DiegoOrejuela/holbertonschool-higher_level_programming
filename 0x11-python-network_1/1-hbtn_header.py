#!/usr/bin/python3
""" Module - hbtn_header"""

if __name__ == "__main__":
    import urllib.request
    from sys import argv

    with urllib.request.urlopen(argv[1]) as response:
        html_header = response.info()
        print(html_header._headers[11][1])
