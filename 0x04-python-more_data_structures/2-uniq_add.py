#!/usr/bin/python3
from functools import reduce
def uniq_add(my_list=[]):
    new_set = set(my_list)
    result = 0
    for x in new_set:
        result += x
    return result
