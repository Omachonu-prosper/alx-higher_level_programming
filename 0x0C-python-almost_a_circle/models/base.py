#!/usr/bin/python3

"""Base module."""


import json


class Base:
    """Base class."""

    __nb_objects = 0

    def __init__(self, id=None):
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @classmethod
    def save_to_file(cls, list_objs):
        """Save JSON string to file."""
        filename = '{}.json'.format(cls.__name__)
        dict_list = []

        if not (list_objs is None or len(list_objs) == 0):
            for obj in list_objs:
                dict_list.append(obj.to_dictionary())

        with open(filename, 'w+') as f:
            json_string = Base.to_json_string(dict_list)
            f.write(json_string)

    @staticmethod
    def to_json_string(list_dictionaries):
        """Dictionary to JSON string."""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return '[]'

        return json.dumps(list_dictionaries)
