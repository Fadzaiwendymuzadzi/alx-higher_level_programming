#!/usr/bin/python3
"""This module  print '#' times the square of a number.

The module has the function print_square.
"""


def print_square(size):
    """Function print_square.

    This function prints the char '#' as many times as
    the square of the given number.

    Args:
        size (int): To stablish the size of the square.

    Returns:
        No return

    """
    if (type(size) != int or size is None):
        raise TypeError("size must be an integer")
    elif (size < 0):
        raise ValueError("size must be >= 0")
    else:
        a = (size * "#") + "\n"
        print(size * a, end="")
