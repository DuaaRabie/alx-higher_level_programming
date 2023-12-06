#!/usr/bin/python3
""" This module convert class to json """


class Student():
    """ This class represents student """
    def __init__(self, first_name, last_name, age):
        """ this function to initialize """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ This function retrieves a dictionary representation """
        return self.__dict__
