#!/usr/bin/python3
"""This module to define a function that adds integers"""


def add_integer(a, b=98):
    """
    This function adds two integers
    """
    if a is None or (type(a) is not int and typy(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and typy(b) is not float:
        raise TypeError("b must be an integer")
    return (int)a + (int)b
