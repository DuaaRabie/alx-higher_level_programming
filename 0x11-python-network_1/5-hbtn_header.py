#!/usr/bin/python3
""" This Module sends request to url and display value """
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)
    headers = response.headers
    print(headers.get("X-Request-Id"))
