#!/usr/bin/pyhton3
"""This module to define a function that adds integers"""


def add_integer(a, b=98):
    """
    This function adds two integers
    >>> add_integer(1, 3)
    4
    >>> add_integer(-1, -2)
    -3
    >>> add_integer(2, -4)
    -2
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return a + b
