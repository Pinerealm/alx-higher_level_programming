#!/usr/bin/python3
"""Unittests for the base module."""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Defines tests for the Base class."""

    def setUp(self):
        """Runs before each test."""
        Base._Base__nb_objects = 0

    def test_id(self):
        """Tests correct id assignment after instantiation."""
        for i in range(1, 20):
            b = Base()
            self.assertEqual(b.id, i)

        b = Base(12)
        self.assertEqual(b.id, 12)

    def test_nb_objects(self):
        """Tests for correct number of objects."""
        for i in range(1, 20):
            b = Base()
            self.assertEqual(Base._Base__nb_objects, i)

        b = Base(12)
        self.assertNotEqual(Base._Base__nb_objects, 20)
