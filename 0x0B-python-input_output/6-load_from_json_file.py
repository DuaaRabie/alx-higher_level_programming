#!/usr/bin/python3
""" This Module create object using json file"""
import json


def load_from_json_file(filename):
    """ This function create object using json file """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
