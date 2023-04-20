#!/usr/bin/python3

"""Tests for the square module."""


import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """Test cases for Square."""

    def test_valid_instantiation(self):
        with self.assertRaises(TypeError):
            Square(10, "2")
        
        with self.assertRaises(ValueError):
            Square(10, 2, -2)

    def test_valid_setters(self):
        r = Square(10, 2)
        with self.assertRaises(ValueError):
            r.width = -10

        with self.assertRaises(TypeError):
            r.x = {}
