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

    def test_valid_update_values(self):
        r1 = Rectangle(10, 10, 10, 10, 10)
        self.assertEqual(str(r1), '[Rectangle] (10) 10/10 - 10/10')
        
        r1.update(89)
        self.assertEqual(str(r1), '[Rectangle] (89) 10/10 - 10/10')
        
        with self.assertRaises(TypeError):
            r1.update(1, 'a string')
        
        with self.assertRaises(TypeError):
            r1.update(width='a string')

    def test_update_args(self):
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

    def test_update_kwargs(self):
        r1 = Rectangle(10, 10, 10, 10, 10)
        self.assertEqual(str(r1), '[Rectangle] (10) 10/10 - 10/10')
        
        r1.update(height=1)
        self.assertEqual(str(r1), '[Rectangle] (10) 10/10 - 10/1')
        
        r1.update(width=1, x=2)
        self.assertEqual(str(r1), '[Rectangle] (10) 2/10 - 1/1')
        
        r1.update(y=1, width=2, x=3, id=89)
        self.assertEqual(str(r1), '[Rectangle] (89) 3/1 - 2/1')
        
        r1.update(x=1, height=2, y=3, width=4)
        self.assertEqual(str(r1), '[Rectangle] (89) 1/3 - 4/2')
        
        r1.update(10, x=5, height=7, y=5, width=6)
        self.assertEqual(str(r1), '[Rectangle] (10) 1/3 - 4/2')
    
    def test_area(self):
        r1 = Rectangle(3, 2)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r1.area(), 6)
        self.assertEqual(r2.area(), 20)
        self.assertEqual(r3.area(), 56)

    def test_to_dictionary(self):
        r1 = Rectangle(10, 2, 1, 9, 1)
        self.assertEqual(r1.to_dictionary(), {'id': 1, 'width': 10, 'height': 2, 'x': 1, 'y': 9})