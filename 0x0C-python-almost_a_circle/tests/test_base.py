#!/usr/bin/python3

"""Test for base module."""


import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    def setUp(self):
        self.base1 = Base()
        self.base2 = Base(10)

    def test_base_id(self):
        self.assertEqual(self.base1.id, 1)
        self.assertEqual(self.base2.id, 10)

    def teatDown(self):
        del self.base1
        del self.base2
