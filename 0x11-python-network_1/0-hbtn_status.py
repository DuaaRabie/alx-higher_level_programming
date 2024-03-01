#!/usr/bin/python3
""" This Module fetches alx intranet """
import urllib.request


url = "https://alx-intranet.hbtn.io/status"
with urllib.request.urlopen(url) as response:
    contents = response.read()
    contents_utf8 = contents.decode('utf-8')
    print("Body response:")
    print("    - type: {}".format(type(contents)))
    print("    - content: {}".format(contents))
    print("    - utf8 content: {}".format(contents_utf8))
