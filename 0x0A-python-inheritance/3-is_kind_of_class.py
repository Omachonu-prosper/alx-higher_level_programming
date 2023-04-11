#!/usr/bin/python3

"""Exports the function <is_kind_of_class(obj, a_class)>."""


def is_kind_of_class(obj, a_class):
    """Returns true if an object is an instance of a specified class.
    or of a class that inherited from it
    False otherwise"""
    return isinstance(obj, a_class)
