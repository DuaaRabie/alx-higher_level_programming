#!/usr/bin/python3
""" This Module saves to json file"""
import json


def save_to_json_file(my_obj, filename):
    """ This function saves to json file """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
