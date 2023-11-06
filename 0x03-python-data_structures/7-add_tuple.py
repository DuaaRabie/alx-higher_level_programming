#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a0, a1, b0, b1 = 0, 0, 0, 0
    if len(tuple_a) >= 2:
        a0, a1 = tuple_a[0], tuple_a[1]
    elif len(tuple_a) == 1:
        a0 = tuple_a[0]

    if len(tuple_b) >= 2:
        b0, b1 = tuple_b[0], tuple_b[1]
    elif len(tuple_b) == 1:
        b0 = tuple_b[0]
    int1 = a0 + b0
    int2 = a1 + b1
    return (int1, int2)
