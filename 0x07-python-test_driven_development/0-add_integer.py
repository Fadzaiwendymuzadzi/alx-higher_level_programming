#!/usr/bin/python3
"""This module has one function to add two integers.

The module has one function add_integer.
"""


def add_integer(a, b=98):
    """Function add integer.

    This functions add two integers or floats.

    Args:
        a (int or float): The first parameter.
        b (int or float): The second parameter.

    Returns:
        int: The return value is an integer addition of the two arguments

    """
    if ((type(a) != int and type(a) != float) or a is None):
        raise TypeError("a must be an integer")
    if ((type(b) != int and type(b) != float) or b is None):
        raise TypeError("b must be an integer")
    if (type(a) == float):
        a = int(a)
    if (type(b) == float):
        b = int(b)
    return a + b
