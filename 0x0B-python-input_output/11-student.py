#!/usr/bin/python3

"""Exports Student class."""


class Student:
    """Clas of students which can be reperesented
    as a dict using to_json method."""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        attributes = vars(self)
        filtered_attrs = {}

        if type(attrs) is list:
            if len(attrs) < 1:
                return filtered_attrs

            for i in attrs:
                if type(i) is not str:
                    return attributes

                if eval("attributes.get('{}')".format(i)):
                    filtered_attrs[i] = eval("attributes.get('{}')".format(i))
            return filtered_attrs
        return attributes

    def reload_from_json(self, json):
        for key, val in json.items():
            self.key = val
