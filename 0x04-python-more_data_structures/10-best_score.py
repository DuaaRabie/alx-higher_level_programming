#!/usr/bin/python3
def best_score(a_dictionary):
    result = None
    if a_dictionary is not None:
        best = float('-inf')
        for x in a_dictionary:
            if a_dictionary[x] > best:
                result = x
                best = a_dictionary[x]
    return result
