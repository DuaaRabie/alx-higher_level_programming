#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    inset1 = [x for x in set_1 if x not in set_2]
    inset2 = [x for x in set_2 if x not in set_1]
    return inset1 + inset2
