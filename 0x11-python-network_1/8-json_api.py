#!/usr/bin/python3
""" This Module sends request to url and display value """
import sys
import requests
import json


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    if len(sys.argv) > 1:
        letter = sys.argv[2]
    else:
        letter = ""
    data = {"q": letter}
    response = requests.post(url, data)
    try:
        res_json = response.json()
    except requests.exceptions.JSONDecodeError as e:
        print("Not a valid JSON")

    if not res_json:
        print("No result")
    else:
        print("[{}] {}".format(res_json.get("id"), res_json.get("name")))
