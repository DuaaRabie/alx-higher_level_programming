#!/usr/bin/python3
def best_score(a_dictionary):
    result = None
    if a_dictionary is not None:
        first =  list(a_dictionary.keys())[0]
        best = a_dictionary[first]
        for x in a_dictionary:
            if a_dictionary[x] > best:
                result = x
    return result
