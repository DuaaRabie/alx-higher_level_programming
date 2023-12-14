#!/usr/bin/python3
""" This module for square """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ This class for Square """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self._size = value
        self.width = value
        self.height = value

    def __str__(self):
        """ This method represents the squar"""
        str_rep = "[Square] ({}) {}/{}".format(self.id, self.x, self.y)
        str_rep += " - {}".format(self.width)
        return str_rep
