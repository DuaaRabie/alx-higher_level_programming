#!/usr/bin/python3
""" This module improve geomety"""


class BaseGeometry():
    """ This class to improve geomety"""
    def area(self):
        """ this function for area exception """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ this function validate value """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
