#!/usr/bin/python3

"""Exports a function that adds a new attribute to an object if possible."""


def add_attribute(a_class, attribute, value):
    """Add a new attribute to a function if possible."""
    if type(a_class) in [int, str, bool, float]:
        raise TypeError('can\'t add new attribute')

    setattr(a_class, attribute, value)
