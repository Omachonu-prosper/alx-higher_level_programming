#!/usr/bin/python3
"""Unittest for max_integer([..])
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_empty_list(self):
        max = max_integer()
        self.assertEqual(max, None)

    def test_all_elements_are_equal(self):
        arr = [1, 1, 1, 1]
        max = max_integer(arr)
        self.assertEqual(max, 1)

    def test_mixed_array(self):
        arr = [1, 'h', 3, 5]

        with self.assertRaises(TypeError):
            max_integer(arr)
