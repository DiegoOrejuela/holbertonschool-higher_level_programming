#!/usr/bin/python3
""" Module - hbtn_header"""

if __name__ == "__main__":
    from sys import argv
    import urllib.parse
    import urllib.request

    url = argv[1]
    values = {'email': argv[2]}

    data = urllib.parse.urlencode(values).encode("utf-8")
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        the_page = response.read()
        print(the_page.decode())
