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

    def test_one_element(self):
        arr = [3]
        max = max_integer(arr)
        self.assertEqual(max, 3)

    def test_one_negative_number(self):
        arr = [1, 2, -3, 4, 5]
        max = max_integer(arr)
        self.assertEqual(max, 5)

    def test_max_at_end(self):
        arr = [4, 5, 3, 2, 10]
        max = max_integer(arr)
        self.assertEqual(max, 10)

    def test_max_at_beginning(self):
        arr = [10, 4, 5, 6]
        max = max_integer(arr)
        self.assertEqual(max, 10)

    def test_max_at_mid(self):
        arr = [1, 2, 10, 4, 5]
        max = max_integer(arr)
        self.assertEqual(max, 10)

    def test_negative_only(self):
        arr = [-1, -2, -3, -4, -5]
        max = max_integer(arr)
        self.assertEqual(max, -1)

    def test_mixed_array(self):
        arr = [1, 'h', 3, 5]

        with self.assertRaises(TypeError):
            max_integer(arr)
