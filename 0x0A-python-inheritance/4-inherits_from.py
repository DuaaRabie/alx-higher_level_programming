#!/usr/bin/python3
""" This module check sub class"""


def inherits_from(obj, a_class):
    """ function to check inheritance """
    if isinstance(obj, a_class) and type(obj) is not a_class:
        return True
    return False
