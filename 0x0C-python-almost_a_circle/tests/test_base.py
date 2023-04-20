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

    def teatDown(self):
        del self.base1
        del self.base2
