#!/usr/bin/python3
"""This module to define a function that adds integers"""


def add_integer(a=0, b=98):
    """
    This function adds two integers
    """
    if a is None or (type(a) is not int and type(a) is not float):
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
