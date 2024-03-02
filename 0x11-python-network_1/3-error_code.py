#!/usr/bin/python3
""" This Module sends request to url and display value """
import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    request = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(request) as response:
            contents = response.read()
            contents_utf8 = contents.decode("utf-8")
            print(contents_utf8)
    except urllib.error.HTTPError as error:
        print("Error code: {}".format(error.code))
