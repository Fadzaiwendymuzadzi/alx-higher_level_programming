#!/usr/bin/python3
"""This module has one function matrix_divided.

The module has one function matrix_divided.
"""


def matrix_divided(matrix, div):
    """Function matrix_divided.

    This function divides all elements in the matrix by a
    given integer:

    Args:
        matrix (matrix): 2D list of integer or floats.
        div (int or float): Multiply each element

    Returns:
        matrix: The return value is a matrix

    """
    str1 = "matrix must be a matrix (list of lists)"
    str2 = "of integers/floats"
    my_matrix = []
    my_row = []
    if (len(matrix) == 0):
        raise TypeError(str1 + " " + str2)
    if (type(matrix[0]) != list):
        raise TypeError(str1 + " " + str2)
    if (len(matrix[0]) == 0):
        raise TypeError(str1 + " " + str2)
    if (div == 0):
        raise ZeroDivisionError("division by zero")
    if ((type(div) != int and type(div) != float) or div is None):
        raise TypeError("div must be a number")
    a = len(matrix[0])
    for row in matrix:
        if (type(row) != list):
            raise TypeError(str1 + " " + str2)
        if (len(row) == 0):
            raise TypeError(str1 + " " + str2)
        if (len(row) != a):
            raise TypeError("Each row of the matrix must have the same size")
        a = len(row)
        for x in row:
            if (type(x) != int and type(x) != float):
                raise TypeError(str1 + " " + str2)
            my_row.append(round((x / div), 2))
        my_matrix.append(my_row)
        my_row = []
    return (my_matrix)
