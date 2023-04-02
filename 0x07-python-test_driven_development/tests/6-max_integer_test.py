#!/usr/bin/python3
"""Unittests for the max_integer function from 6-max_integer.py
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """This class tests the max_integer function."""

    def test_max_integer(self):
        """Test the max_integer function.
        """
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([10, 2, 5, 1]), 10)
        self.assertEqual(max_integer([4]), 4)

        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer(), None)
