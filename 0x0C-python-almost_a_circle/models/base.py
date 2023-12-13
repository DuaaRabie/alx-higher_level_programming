#!/usr/bin/python3
""" This is the base module"""


class Base():
    """ This is the base class"""
    __nb_objects = 0

    @classmethod
    def increment_nb_objects(cls):
        cls.__nb_objects += 1

    def __init__(self, id=None):
        """ This is the constructor """
        if id is not None:
            self.id = id
        else:
            self.increment_nb_objects()
            self.id = self.__nb_objects
