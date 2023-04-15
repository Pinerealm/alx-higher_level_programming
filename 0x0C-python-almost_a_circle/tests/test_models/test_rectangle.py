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
        for i in range(1, 20):
            r = Rectangle(1, 1)
            self.assertEqual(r.id, i)

        r = Rectangle(1, 1, 0, 0, 12)
        self.assertEqual(r.id, 12)

    def test_width(self):
        """Test correct width assignment."""
        for i in range(1, 20):
            r = Rectangle(i, 1)
            self.assertEqual(r.width, i)

        r.width = 10
        self.assertEqual(r.width, 10)
        self.assertRaises(TypeError, Rectangle, "1", 1)
        self.assertRaises(ValueError, Rectangle, 0, 1)

    def test_height(self):
        """Test correct height assignment."""
        for i in range(1, 20):
            r = Rectangle(1, i)
            self.assertEqual(r.height, i)

        r.height = 10
        self.assertEqual(r.height, 10)
        self.assertRaises(TypeError, Rectangle, 1, "1")
        self.assertRaises(ValueError, Rectangle, 1, 0)

    def test_x(self):
        """Test correct x coordinate assignment."""
        for i in range(0, 20):
            r = Rectangle(1, 1, i)
            self.assertEqual(r.x, i)

        r.x = 5
        self.assertEqual(r.x, 5)
        self.assertRaises(TypeError, Rectangle, 1, 1, "1")
        self.assertRaises(ValueError, Rectangle, 1, 1, -1)

    def test_y(self):
        """Test correct y coordinate assignment."""
        for i in range(0, 20):
            r = Rectangle(1, 1, 0, i)
            self.assertEqual(r.y, i)

        r.y = 6
        self.assertEqual(r.y, 6)
        self.assertRaises(TypeError, Rectangle, 1, 1, 1, "1")
        self.assertRaises(ValueError, Rectangle, 1, 1, 1, -1)

    def test_area(self):
        """Test correct area calculation."""
        for i in range(1, 20):
            r = Rectangle(i, i)
            self.assertEqual(r.area(), i * i)
