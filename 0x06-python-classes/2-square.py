#!/usr/bin/python3
""" This Module define class Square """


class Square:
    """ This Method defines a Square"""
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
