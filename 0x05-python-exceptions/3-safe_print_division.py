#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        print("Inside result: ", end="")
        result = a / b
        return result
    except ZeroDivisionError:
        result = None
    finally:
        print("{}".format(result))
