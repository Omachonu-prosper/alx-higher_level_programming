#!/usr/bin/python3

"""Test the validateValue static function of the Rectangle class."""


import unittest
from models.rectangle import Rectangle


class TestValidateValue(unittest.TestCase):
    def test_not_int(self):
        with self.assertRaises(TypeError):
            Rectangle.validateValue('a string', 'width')

    def test_not_valid_type(self):
        with self.assertRaises(ValueError):
            Rectangle.validateValue(1, 'invalid type')

    def test_negative_width(self):
        with self.assertRaises(ValueError):
            Rectangle.validateValue(-1, 'width')

    def test_negative_x(self):
        with self.assertRaises(ValueError):
            Rectangle.validateValue(-1, 'x')