#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    to_delete = [x for x, y in a_dictionary.items() if y != value]
    for key in to_delete:
        del a_dictionary[key]
    return a_dictionary
