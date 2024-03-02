#!/usr/bin/python3
""" This Module sends request to url and display value """
import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    values = {"email": email}
    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')
    request = urllib.request.Request(url, data)
    with urllib.request.urlopen(request) as response:
        contents = response.read()
        contents_utf8 = contents.decode("utf-8")
        print(contents_utf8)
