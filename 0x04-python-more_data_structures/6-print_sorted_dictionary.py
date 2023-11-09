#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sortdic = sorted(a_dictionary)
    for x in sortdic:
        print("{}: {}".format(x, a_dictionary.get(x)))
