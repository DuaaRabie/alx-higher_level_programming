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
    try:
        res_json = response.json()
    except ValueError:
        print("Not a valid JSON")
        sys.exit(1)

    if not res_json:
        print("No result")
    else:
        print(res_json.get("id"))
