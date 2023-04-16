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

    def test_save_to_file(self):
        """Tests correct file writing."""
        import os
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")

        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")
        os.remove("Rectangle.json")

        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")
        os.remove("Rectangle.json")

        r = Rectangle(1, 2, 3, 4, 5)
        r2 = Rectangle(6, 7, 8, 9, 10)
        Rectangle.save_to_file([r, r2])
        result = '[{"id": 5, "width": 1, "height": 2, "x": 3, "y": 4}, '
        result += '{"id": 10, "width": 6, "height": 7, "x": 8, "y": 9}]'
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), result)
        os.remove("Rectangle.json")

        if os.path.exists("Square.json"):
            os.remove("Square.json")

        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), "[]")
        os.remove("Square.json")

        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), "[]")
        os.remove("Square.json")

        s = Square(1, 2, 3, 4)
        s2 = Square(5, 6, 7, 8)
        Square.save_to_file([s, s2])
        result = '[{"id": 4, "size": 1, "x": 2, "y": 3}, '
        result += '{"id": 8, "size": 5, "x": 6, "y": 7}]'
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), result)
        os.remove("Square.json")

    def test_from_json_string(self):
        """Tests correct JSON string to list conversion."""
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string("[]"), [])

        j_str = '[{"id": 5, "width": 2, "height": 3, "x": 1, "y": 1}, '
        j_str += '{"id": 4, "width": 4, "height": 2, "x": 2, "y": 2}]'
        o_list = [{"id": 5, "width": 2, "height": 3, "x": 1, "y": 1},
                  {"id": 4, "width": 4, "height": 2, "x": 2, "y": 2}]
        self.assertEqual(Base.from_json_string(j_str), o_list)
        self.assertIsInstance(Base.from_json_string(j_str), list)

        r1 = Rectangle(1, 2, 3, 4, 5)
        r2 = Rectangle(6, 7, 8, 9, 10)
        r_list = [r1.to_dictionary(), r2.to_dictionary()]
        r_str = r1.to_json_string(r_list)
        self.assertEqual(r1.from_json_string(r_str), r_list)
        self.assertIsInstance(r1.from_json_string(r_str), list)

        s1 = Square(1, 2, 3, 4)
        s2 = Square(5, 6, 7, 8)
        s_list = [s1.to_dictionary(), s2.to_dictionary()]
        s_str = s1.to_json_string(s_list)
        self.assertEqual(s1.from_json_string(s_str), s_list)
        self.assertIsInstance(s1.from_json_string(s_str), list)

    def test_create(self):
        """Tests correct object creation from a dictionary."""
        r = Rectangle(1, 2, 3, 4, 5)
        r_d = r.to_dictionary()
        r2 = Rectangle.create(**r_d)
        self.assertEqual(r2.to_dictionary(), r_d)
        self.assertIsNot(r2, r)

        s = Square(1, 2, 3, 4)
        s_d = s.to_dictionary()
        s2 = Square.create(**s_d)
        self.assertEqual(s2.to_dictionary(), s_d)
        self.assertIsNot(s2, s)
