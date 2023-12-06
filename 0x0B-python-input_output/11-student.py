#!/usr/bin/python3
""" This module convert class to json """


class Student():
    """ This class represents student """
    def __init__(self, first_name, last_name, age):
        """ this function to initialize """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ This function retrieves a dictionary representation """
        if attrs is None:
            return self.__dict__
        result = {}
        for attr in attrs:
            if hasattr(self, attr):
                result[attr] = getattr(self, attr)
        return result

    def reload_from_json(self, json):
        for attr, value in json.items():
            setattr(self, attr, value)
