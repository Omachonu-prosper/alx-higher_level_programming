#!/usr/bin/python3

"""Exports the function <is_same_class(obj, a_class)>."""


def is_same_class(obj, a_class):
    """Returns true if an object is exactly an instance of a specified class.
    False otherwise"""
    if a_class == object and obj is not object:
        return False

    return isinstance(obj, a_class)
