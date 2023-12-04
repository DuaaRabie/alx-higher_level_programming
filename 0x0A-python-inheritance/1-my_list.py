#!/usr/bin/python3
""" This module to inherit from list class """


class MyList(list):
    """ This class inherits from list class """
    def print_sorted(self):
        """ This function prints the list"""
        print(sorted(self))
