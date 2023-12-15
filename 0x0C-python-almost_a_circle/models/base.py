#!/usr/bin/python3
""" This is the base module"""
import json
import os


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
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

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

    @staticmethod
    def from_json_string(json_string):
        """ This method returns the list dict of the json string"""
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ This method returns instance for a dictionary"""
        name = cls.__name__
        if name == "Rectangle":
            dummy = cls(width=1, height=1)
        elif name == "Square":
            dummy = cls(size=3)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ This method returns list of instances"""
        file_name = cls.__name__ + ".json"
        if not os.path.exists(file_name):
            return []
        else:
            with open(file_name, "r") as f:
                data = f.read()
            strings = data.split('\n')
            lists = [cls.from_json_string(string) for string in strings]
            return [cls.create(**dic) for dics in lists for dic in dics]
