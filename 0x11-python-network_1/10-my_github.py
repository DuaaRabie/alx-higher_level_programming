#!/usr/bin/python3
""" This Module sends request to url and display value """
import sys
import requests


if __name__ == "__main__":
    url = "https://api.github.com/user"
    username = sys.argv[1]
    password = sys.argv[2]
    auth = (username, password)
    response = requests.post(url, auth=auth)
    if response.status_code == 200:
        res_json = response.json()
        print(res_json.get("id"))
