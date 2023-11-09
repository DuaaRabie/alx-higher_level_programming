#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    a_dictionary = {x: y for x, y in a_dictionary.items() if y != value}
    return a_dictionary
