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
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b3 = Base(12)
        self.assertEqual(b3.id, 12)
        b4 = Base()
        self.assertEqual(b4.id, 3)

        b5 = Base()
        self.assertNotEqual(b5.id, 3)

    def test_nb_objects(self):
        """Tests for correct number of objects."""
        b1 = Base()
        self.assertEqual(Base._Base__nb_objects, 1)
        b2 = Base()
        self.assertEqual(Base._Base__nb_objects, 2)
        b3 = Base(12)
        self.assertEqual(Base._Base__nb_objects, 2)
        b4 = Base()
        self.assertEqual(Base._Base__nb_objects, 3)

        b5 = Base()
        self.assertNotEqual(Base._Base__nb_objects, 3)
