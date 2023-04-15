"""Unittests for the rectangle module."""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Defines tests for the Rectangle class."""

    def setUp(self):
        """Runs before each test."""
        Base._Base__nb_objects = 0

    def test_id(self):
        """Test correct id assignment after instantiation."""
        r1 = Rectangle(1, 1)
        self.assertEqual(r1.id, 1)
        r2 = Rectangle(1, 1)
        self.assertEqual(r2.id, 2)
        r3 = Rectangle(1, 1, 0, 0, 12)
        self.assertEqual(r3.id, 12)
        r4 = Rectangle(1, 1)
        self.assertEqual(r4.id, 3)

        r5 = Rectangle(1, 1)
        self.assertNotEqual(r5.id, 3)

    def test_width(self):
        """Test correct width assignment."""
        r1 = Rectangle(1, 1)
        self.assertEqual(r1.width, 1)
        r2 = Rectangle(2, 1)
        self.assertEqual(r2.width, 2)
        r3 = Rectangle(3, 1)
        self.assertEqual(r3.width, 3)
        r2.width = 10
        self.assertEqual(r2.width, 10)

    def test_height(self):
        """Test correct height assignment."""
        r1 = Rectangle(1, 1)
        self.assertEqual(r1.height, 1)
        r2 = Rectangle(1, 2)
        self.assertEqual(r2.height, 2)
        r3 = Rectangle(1, 3)
        self.assertEqual(r3.height, 3)
        r2.height = 10
        self.assertEqual(r2.height, 10)

    def test_x(self):
        """Test correct x coordinate assignment."""
        r1 = Rectangle(1, 1)
        self.assertEqual(r1.x, 0)
        r2 = Rectangle(1, 1, 2)
        self.assertEqual(r2.x, 2)
        r3 = Rectangle(1, 1, 3)
        self.assertEqual(r3.x, 3)
        r2.x = 10
        self.assertEqual(r2.x, 10)

    def test_y(self):
        """Test correct y coordinate assignment."""
        r1 = Rectangle(1, 1)
        self.assertEqual(r1.y, 0)
        r2 = Rectangle(1, 1, 0, 2)
        self.assertEqual(r2.y, 2)
        r3 = Rectangle(1, 1, 0, 3)
        self.assertEqual(r3.y, 3)
        r2.y = 10
        self.assertEqual(r2.y, 10)
