#!/usr/bin/python3
""" This Module represents object"""
import json


def from_json_string(my_str):
    """ This function returns object using json representation """
    obj = json.loads(my_str)
    return obj
