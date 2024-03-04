#!/usr/bin/python3
""" This Module sends request to url and display value """
import sys
import requests


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    url = f"https://api.github.com/users/{username}"
    headers = {'Authorization': f'password {password}'}
    response = requests.post(url, headers=headers)
    res_json = response.json()
    if not response.status_code == 200:
        print(res_json.get("id"))
