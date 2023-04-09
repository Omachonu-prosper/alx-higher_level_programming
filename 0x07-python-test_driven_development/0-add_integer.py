#!/usr/bin/python3

"""This Module makes available a funtion to add two values.

The values must be integers or floats.
"""


def add_integer(a, b=98):
    """Adds two numbers together

    a and b must be integers or floats
    otherwise raise a TypeError exception with the message
    a must be an integer
    or b must be an integer
    a and b must be first casted to integers if they are float

    Example:
    >>> add_integer(1, 2)
    3
    """
    if not (type(a) is int or type(a) is float):
        raise TypeError('a must be an integer')
    if not (type(b) is int or type(b) is float):
        raise TypeError('b must be an integer')

    return int(a) + int(b)
