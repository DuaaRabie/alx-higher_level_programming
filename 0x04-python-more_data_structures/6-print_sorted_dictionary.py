#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sortdic = sorted(a_dictionary.keys())
    if sortdic is not None:
        for x in sortdic:
            print("{}: {}".format(x, a_dictionary.get(x)))
