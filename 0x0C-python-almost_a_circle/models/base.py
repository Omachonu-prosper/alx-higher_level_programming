#!/usr/bin/python3

"""Base module."""


class Base:
    """Base class."""
    
    __nb_objects = 0

    def __init__(self, id=None):
        if id is None:
            self.id = self.__nb_objects + 1
        else:
            self.id = id
