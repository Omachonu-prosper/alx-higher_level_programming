#!/usr/bin/python3

"""Tests for the rectangle module."""


import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test cases for Rectangle."""

    def test_valid_instantiation(self):
        with self.assertRaises(TypeError):
            Rectangle(10, "2")
        
        with self.assertRaises(ValueError):
            Rectangle(10, 2, 3, -1)

    def test_valid_setters(self):
        r = Rectangle(10, 2)
        with self.assertRaises(ValueError):
            r.width = -10

        with self.assertRaises(TypeError):
            r.x = {}

    def test_update(self):
        r1 = Rectangle(10, 10, 10, 10, 10)
        self.assertEqual(str(r1), '[Rectangle] (10) 10/10 - 10/10')
        r1.update(89)
        self.assertEqual(str(r1), '[Rectangle] (89) 10/10 - 10/10')
        r1.update(89, 2)
        self.assertEqual(str(r1), '[Rectangle] (89) 10/10 - 2/10')
        r1.update(89, 2, 3)
        self.assertEqual(str(r1), '[Rectangle] (89) 10/10 - 2/3')
        r1.update(89, 2, 3, 4)
        self.assertEqual(str(r1), '[Rectangle] (89) 4/10 - 2/3')
        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r1), '[Rectangle] (89) 4/5 - 2/3')
    
    def test_area(self):
        r1 = Rectangle(3, 2)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r1.area(), 6)
        self.assertEqual(r2.area(), 20)
        self.assertEqual(r3.area(), 56)