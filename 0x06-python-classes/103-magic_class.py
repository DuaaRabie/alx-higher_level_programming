#!/usr/bin/python3
""" This Module defines MagicClass"""


class MagicClass:
    """This class defines magic class"""
    def __init__(self, radius=0):
        self._MagicClass__radius = 0
        if not isinstance(radius, (int, float)):
            raise TypeError('radius must be a number')
        else:
            self._MagicClass__radius = radius
        return None

    """This Method computes the area"""
    def area(self):
        return (self._MagicClass__radius ** 2) * math.pi

    """This Method compute circumference"""
    def circumference(self):
        return 2 * math.pi * self._MagicClass__radius
