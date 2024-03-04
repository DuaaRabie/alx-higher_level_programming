#!/usr/bin/python3
""" This Module sends request to url and display value """
import sys
import requests


if __name__ == "__main__":
    url = "https://api.github.com"
    repository_name = sys.argv[1]
    owner_name = sys.argv[2]
    url = f"{url}/repos/{owner_name}/{repository_name}/commits"
    response = requests.post(url)
    commits = response.json()
    for commit in commits:
        print("{}: {}".format(commit['sha'], commit['commit']['author']['name']))
