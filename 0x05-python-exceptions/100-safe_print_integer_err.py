#!/usr/bin/python3
def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
    except ValueError as s:
        print("Exception:", s)
        return False

    return True
