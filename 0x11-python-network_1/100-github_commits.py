#!/usr/bin/python3
""" This Module sends request to url and display value """
import sys
import requests


if __name__ == "__main__":
    url = "https://developer.github.com/v3/repos/commits/"
    repository_name = sys.argv[1]
    owner_name = sys.argv[2]
    auth = (repository_name, owner_name)
    response = requests.post(url, auth=auth)
    try:
        res_json = response.json()
    except ValueError:
        print("Not a valid JSON")
        sys.exit(1)

    if not res_json:
        print("No result")
    else:
        print("{}: {}".format(res_json.get("sha"), res_json("author_name")))
