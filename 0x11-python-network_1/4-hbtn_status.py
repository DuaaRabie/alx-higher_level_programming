#!/usr/bin/python3
""" This Module fetches alx intranet """
import requests


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    response = requests.get(url)
    contents = response.text
    print("Body response:")
    print("\t- type: {}".format(type(contents)))
    print("\t- content: {}".format(contents))
