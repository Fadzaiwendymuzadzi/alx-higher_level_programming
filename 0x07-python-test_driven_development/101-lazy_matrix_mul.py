#!/usr/bin/python3

"""This module has one function lazy_matrix_mul"""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Function lazy_matrix_mul:

    Args:
        m_a (2D array): The first parameter.
        m_b (2D array): The second parameter

    Returns:
        my_matrix: The return value is a new matrix
    """
    my_matrix = []
    m = 0

    if (len(m_a) == 0 or len(m_a[0]) == 0):
        raise ValueError("m_a can't be empty")
    if (len(m_b) == 0 or len(m_b[0]) == 0):
        raise ValueError("m_b can't be empty")
    if (isinstance(m_a, list) is False):
        raise TypeError("m_a must be a list")
    if (isinstance(m_b, list) is False):
        raise TypeError("m_b must be a list")
    if (isinstance(m_a[0], list) is False):
        raise TypeError("m_a must be a list of lists")
    if (isinstance(m_b[0], list) is False):
        raise TypeError("m_b must be a list of lists")
    la = len(m_a[0])
    lb = len(m_b[0])
    for i in range(len(m_a)):
        if (len(m_a[i]) != len(m_b)):
            raise ValueError("m_a and m_b can't be multiplied")
        if (len(m_a[i]) != la):
            raise TypeError("each row of m_a must be of the same size")
        for j in range(len(m_b[0])):
            if (len(m_b[j]) != lb):
                raise TypeError("each row of m_b must be of the same size")
            for z in range(len(m_b)):
                if (type(m_a[i][z]) != int and type(m_a[i][z]) != float):
                    raise TypeError("m_a should contain only integers or floats")
                if (type(m_b[z][j]) != int and type(m_b[z][j]) != float):
                    raise TypeError("m_b should contain only integers or floats")
    my_matrix = np.dot(m_a, m_b)
    return my_matrix
