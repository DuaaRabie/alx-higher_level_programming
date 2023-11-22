#!/usr/bin/python3
""" This Module define class Square """


class Square:
    """ This Method defines a Square"""
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    """ This Method returns the current square area """
    def area(self):
        return self.__size ** 2

    """ This Method prints in stdout the square with the character #"""
    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print(self.size * "#")
