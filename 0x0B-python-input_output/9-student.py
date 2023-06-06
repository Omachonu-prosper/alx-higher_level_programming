#!/usr/bin/python3

"""Exports Student class."""


class Student:
    """Clas of students which can be reperesented
    as a dict using to_json method."""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return vars(self)
