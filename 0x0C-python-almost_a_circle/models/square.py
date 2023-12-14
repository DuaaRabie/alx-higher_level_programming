#!/usr/bin/python3
""" This module for square """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ This class for Square """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ This is the size getter """
        return self.width

    @size.setter
    def size(self, value):
        """ This is the size setter """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def __str__(self):
        """ This method represents the squar"""
        str_rep = "[Square] ({}) {}/{}".format(self.id, self.x, self.y)
        str_rep += " - {}".format(self.width)
        return str_rep

    def update(self, *args, **kwargs):
        """ This method to update square """
        if kwargs and (not args or args is None):
            for key, value in kwargs.items():
                setattr(self, key, value)
        for i, value in enumerate(args):
            setattr(self, ['id', 'size', 'x', 'y'][i], value)

    def to_dictionary(self):
        """ This mehtod returns the dictionary representation """
        dic1 = ['id', 'x', 'size', 'y']
        dic2 = [self.id, self.x, self.width, self.y]
        return dict(zip(dic1, dic2))
