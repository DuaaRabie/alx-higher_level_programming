#!/usr/bin/python3
""" This module divide Matrix """


def matrix_divided(matrix, div):
    """ This function return the division of Matrix """
    if type(matrix) is not list or\
            (not all(type(x) is int for row in matrix for x in row) and \
            not all(type(x) is float for row in matrix for x in row)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not type(div) is int and not type(div) is float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new = [row[:] for row in matrix]
    for i in range(len(new)):
        for j in range(len(new)):
            new[i][j] = round(new[i][j] / div, 2)
    return new
