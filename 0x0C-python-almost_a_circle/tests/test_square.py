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

    def test_size_getter(self):
        r = Square(10)
        self.assertEqual(r.size, 10)
        r.size = 20
        self.assertEqual(r.size, 20)

    def test_size_setter(self):
        r = Square(10)
        
        with self.assertRaises(TypeError):
            r.size = 'a string'

        with self.assertRaises(ValueError):
            r.size = -5

    def test_valid_update_values(self):
        r1 = Square(10, 10, 10, 10)
        self.assertEqual(str(r1), '[Square] (10) 10/10 - 10')
        
        r1.update(89)
        self.assertEqual(str(r1), '[Square] (89) 10/10 - 10')
        
        with self.assertRaises(TypeError):
            r1.update(1, 'a string')
        
        with self.assertRaises(TypeError):
            r1.update(size='a string')

    def test_update_args(self):
        r1 = Square(10, 10, 10, 10)
        self.assertEqual(str(r1), '[Square] (10) 10/10 - 10')
        
        r1.update(89)
        self.assertEqual(str(r1), '[Square] (89) 10/10 - 10')
        
        r1.update(89, 2)
        self.assertEqual(str(r1), '[Square] (89) 10/10 - 2')
        
        r1.update(89, 2, 3)
        self.assertEqual(str(r1), '[Square] (89) 3/10 - 2')
        
        r1.update(89, 2, 3, 4)
        self.assertEqual(str(r1), '[Square] (89) 3/4 - 2')

    def test_update_kwargs(self):
        r1 = Square(10, 10, 10, 10)
        self.assertEqual(str(r1), '[Square] (10) 10/10 - 10')
        
        r1.update(size=1)
        self.assertEqual(str(r1), '[Square] (10) 10/10 - 1')
        
        r1.update(y=1, size=2, x=3, id=89)
        self.assertEqual(str(r1), '[Square] (89) 3/1 - 2')
        
        r1.update(10, x=5, y=5, size=6)
        self.assertEqual(str(r1), '[Square] (10) 3/1 - 2')
    
    def test_area(self):
        r1 = Square(3)
        r2 = Square(2)
        r3 = Square(8, 0, 0, 12)
        self.assertEqual(r1.area(), 9)
        self.assertEqual(r2.area(), 4)
        self.assertEqual(r3.area(), 64)
