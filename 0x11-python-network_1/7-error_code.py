#!/usr/bin/python3
""" This Module sends request to url and display value """
import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    try:
        response = requests.get(url)
        contents = response.text
        print(contents)
    except urllib.error.HTTPError as error:
        print("Error code: {}".format(error.code))
