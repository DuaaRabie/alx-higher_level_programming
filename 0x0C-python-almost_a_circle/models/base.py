#!/usr/bin/python3
""" This is the base module"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or list_dictionaries == {}:
            return "[]"
        repre = json.dumps(list_dictionaries)
        return repre        
