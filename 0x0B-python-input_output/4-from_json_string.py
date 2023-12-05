#!/usr/bin/python3
import json
""" This Module represents to json """


def to_json_string(my_obj):
    """ This function returns json representation """
    obj_str = json.dumps(my_obj)
    return obj_str
