#!/usr/bin/python3
"""This module has the function text_indentation"""


def text_indentation(text):
    """
    Function text_indentation:

    Args:
        text (str): string to be split

    Returns:
        prints a text with 2 new lines after  characters: ., ? and :
    """

    str_new = ""
    flag_spa = 0
    m = 0
    if (type(text) != str or text is None):
        raise TypeError("text must be a string")
    else:
        for i in text:
            if (i != " "):
                flag_spa = 2
            if (flag_spa == 2):
                str_new = str_new + i
            if (i == '?' or i == '.' or i == ':'or m == (len(text) - 1)):
                k = len(text) - 1
                if (m == k and i != '?' and i != '.' and i != ':'):
                    print(str_new, end="")
                else:
                    print(str_new)
                    print("")
                str_new = ""
                flag_spa = 1
            m += 1
