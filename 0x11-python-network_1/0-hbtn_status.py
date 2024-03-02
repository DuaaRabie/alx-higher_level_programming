#!/usr/bin/python3
""" This Module fetches alx intranet """
import urllib.request


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    with urllib.request.urlopen(url) as response:
        contents = response.read()
        contents_utf8 = contents.decode('utf-8')
        print("Body response:")
        print("\t-type: {}".format(type(contents)))
        print("\t-content: {}".format(contents))
        print("\t-utf8 content: {}".format(contents_utf8))
