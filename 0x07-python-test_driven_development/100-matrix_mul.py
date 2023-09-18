#!/usr/bin/python3
"""This module compute the multiplication of two matrix.

This module has one function matrix_mul.
"""


def matrix_mul(m_a, m_b):
    """Function matrix_mul.

    This function will check valid arguments and
    return the multiplication of two matrix.

    Args:
        m_a (2D array): The first parameter.
        m_b (2D array): The second parameter

    Returns:
        my_matrix: The return value is a new matrix

    """
    my_matrix = []
    my_row = []
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
                m +=  m_a[i][z] * m_b[z][j]
            my_row.append(m)
            m = 0
        my_matrix.append(my_row)
        my_row = []
    return my_matrix
