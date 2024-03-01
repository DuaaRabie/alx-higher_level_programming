#!/usr/bin/python3
""" This module divide Matrix """


def matrix_divided(matrix, div=1):
    """ This function return the division of Matrix """
    if type(matrix) is not list or (len(matrix) == 0) or\
            type(matrix[0]) is not list or (len(matrix[0]) == 0):
        raise TypeError("matrix must be a matrix "
                       "(list of lists) of integers/floats")
    for row in matrix:
        if type(row) is not list:
            raise TypeError("matrix must be a matrix "
                           "(list of lists) of integers/floats")
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for x in row:
            if type(x) is not int and type(x) is not float:
                raise TypeError("matrix must be a matrix "
                               "(list of lists) of integers/floats")

    if not type(div) is int and not type(div) is float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new = [row[:] for row in matrix]
    for i in range(len(new)):
        for j in range(len(new)):
            new[i][j] = round(new[i][j] / div, 2)
    return new
