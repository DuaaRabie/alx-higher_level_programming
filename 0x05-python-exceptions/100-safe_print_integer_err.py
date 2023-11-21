#!/usr/bin/python3
def safe_print_integer_err(value):
    import sys
    try:
        print("{:d}".format(value))
    except ValueError as s:
        print("Exception:", s, file=sys.stderr)
        return False

    return True
