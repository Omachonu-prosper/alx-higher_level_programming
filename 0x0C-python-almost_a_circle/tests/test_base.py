#!/usr/bin/python3

"""Test for base module."""


import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Test class for Base class."""

    def setUp(self):
        self.base1 = Base()
        self.base2 = Base(10)
        self.base3 = Base()

    def test_base_id(self):
        self.assertEqual(self.base1.id, 1)
        self.assertEqual(self.base2.id, 10)
        self.assertEqual(self.base3.id, 2)

    def test_to_json_string(self):
        dictionary = {'x': 2, 'width': 10, 'id': 1, 'height': 7, 'y': 8}
        self.assertEqual(type(dictionary), dict)

        json_dictionary = Base.to_json_string(dictionary)
        self.assertEqual(type(json_dictionary), str)
    
    def test_from_json_string(self):
        list_input = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        self.assertEqual(type(json_list_input), str)

        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(type(list_output), list)

    def teatDown(self):
        del self.base1
        del self.base2
