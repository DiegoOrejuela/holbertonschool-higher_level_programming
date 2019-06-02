#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_last_item_gr(self):
        self.assertEqual(max_integer([4]), 4)

    def test_last_item_gr(self):
        self.assertEqual(max_integer([2, 2, 3, 4]), 4)

    def test_upper(self):
        self.assertEqual(max_integer([2, 3, 4, 1]), 4)

    def test_neg_pos(self):
        self.assertEqual(max_integer([0, 35, -65, -7]), 35)

    def test_only_neg(self):
        self.assertEqual(max_integer([-42, -334, -456, -3341]), -42)

    def test_same_value(self):
        self.assertEqual(max_integer([0, 0, 0, 0, 0]), 0)

    def test_list_empty(self):
        self.assertEqual(max_integer([]), None)

    def test_case_none(self):
        with self.assertRaises(TypeError):
            max_integer(None)

if __name__ == '__main__':
    unittest.main()
