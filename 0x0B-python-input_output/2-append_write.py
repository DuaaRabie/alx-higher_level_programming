#!/usr/bin/python3

def append_write(filename="", text=""):
    """ This function append to file """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
