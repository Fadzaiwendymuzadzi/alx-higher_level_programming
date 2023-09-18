#!/usr/bin/python3
"""This module prints first name and last name.

This module has one function say_my_name.
"""


def say_my_name(first_name, last_name=""):
    """Function say my name.

    This function check the right first and last name
    and prints:

    Args:
        first_name (str): The first parameter has to be string.
        last_name (str): The second parameter has to be string-

    Returns:
        not return

    """
    if (type(first_name) != str or first_name is None):
        raise TypeError("first_name must be a string")
    elif (type(last_name) != str or last_name is None):
        raise TypeError("last_name must be a string")
    else:
        print("My name is {:s} {:s}".format(first_name, last_name))
