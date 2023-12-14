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
        """ This method returns json string representation """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        to_conv = [
                obj.to_dictionary() if not isinstance(obj, dict) else
                obj.__dict__ for obj in list_dictionaries
        ]
        return json.dumps(to_conv)

    @classmethod
    def save_to_file(cls, list_objs):
        """ This method wrtie the json representation """
        file_name = cls.__name__ + ".json"
        if list_objs is None:
            repre = "[]"
        else:
            repre = cls.to_json_string(list_objs)
        with open(file_name, "w") as f:
            f.write(repre)
