#!/usr/bin/python3
""" This Module defines MagicClass"""


class MagicClass:
    """This class """
    def __init(self, radius):
        self._MagicClass__radius = 0

        if type(radius) is not int:
            raise TypeError('radius must be a number')
        else:
            self._MagicClass__radius = radius
