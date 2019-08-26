#!/usr/bin/python3
""" Module - hbtn_header"""

if __name__ == "__main__":
    import urllib.request
    from sys import argv

    with urllib.request.urlopen(argv[1]) as response:
        html_header = response.info()
        for item in html_header._headers:
            if "X-Request-Id" in item[0]:
                print(item[1])
