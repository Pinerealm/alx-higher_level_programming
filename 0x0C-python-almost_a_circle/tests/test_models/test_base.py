#!/usr/bin/python3
"""Unittests for the base module."""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


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
        """Tests for correct count of objects."""
        for i in range(1, 20):
            b = Base()
            self.assertEqual(Base._Base__nb_objects, i)

        b = Base(12)
        self.assertNotEqual(Base._Base__nb_objects, 20)

    def test_to_json_string(self):
        """Tests correct JSON string representation."""
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")

        d = {"id": 1, "width": 2, "height": 3, "x": 4, "y": 5}
        d_str = '[{"id": 1, "width": 2, "height": 3, "x": 4, "y": 5}]'
        self.assertEqual(Base.to_json_string([d]), d_str)
        self.assertIsInstance(Base.to_json_string([d]), str)

        r = Rectangle(1, 2, 3, 4, 5)
        r_d = r.to_dictionary()
        r_str = '[{"id": 5, "width": 1, "height": 2, "x": 3, "y": 4}]'
        self.assertEqual(r.to_json_string([r_d]), r_str)
        self.assertIsInstance(r.to_json_string([r_d]), str)

        s = Square(1, 2, 3, 4)
        s_d = s.to_dictionary()
        s_str = '[{"id": 4, "size": 1, "x": 2, "y": 3}]'
        self.assertEqual(s.to_json_string([s_d]), s_str)
        self.assertIsInstance(s.to_json_string([s_d]), str)
