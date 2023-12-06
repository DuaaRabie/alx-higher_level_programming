#!/usr/bin/python3
""" This module for pascal's triangle """


def pascal_triangle(n):
    """ This function returns pascal triangle """
    if n <= 0:
        return []
    result = [[1]]
    for i in range(1, n):
        add = [result[i - 1][j - 1] + result[i - 1][j] for j in range(1, i)]
        row = [1] + add + [1]
        result.append(row)
    return result
