#!/usr/bin/python3

"""Exports a base class BaseGeometry."""


class BaseGeometry:
    """Base class that other geometry related modules inherit from."""

    def area(self):
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """Validates that value is an integer."""

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
