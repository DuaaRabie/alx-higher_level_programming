#!/usr/bin/python3

""" This Module to write files """


def write_file(filename="", text=""):
    """ This function to write files """
    with open(filename, "w", encoding="utf-8") as f:
        count = f.write(text)
    return count
