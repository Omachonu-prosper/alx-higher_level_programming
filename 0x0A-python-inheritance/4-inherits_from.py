#!/usr/bin/python3

"""Exports the function <inherits_from(obj, a_class)>."""


def inherits_from(obj, a_class):
    """Returns true if an object is an instance of
    a class that inherited (directly or indirectly)
    rom the specified class ; otherwise False."""
    if type(obj) is a_class:
        return False

    return isinstance(obj, a_class)
