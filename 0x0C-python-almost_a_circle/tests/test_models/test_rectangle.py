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

        with self.assertRaises(TypeError) as e:
            Rectangle(1)
        self.assertEqual(str(e.exception), "__init__() missing 1 required "
                                           "positional argument: 'height'")
        with self.assertRaises(TypeError) as e:
            Rectangle()
        self.assertEqual(str(e.exception), "__init__() missing 2 required "
                                           "positional arguments: 'width' and "
                                           "'height'")

    def test_width(self):
        """Test correct width assignment."""
        for i in range(1, 20):
            r = Rectangle(i, 1)
            self.assertEqual(r.width, i)

        r.width = 10
        self.assertEqual(r.width, 10)
        with self.assertRaises(TypeError) as e:
            Rectangle("1", 1)
        self.assertEqual(str(e.exception), "width must be an integer")
        with self.assertRaises(ValueError) as e:
            Rectangle(0, 1)
        self.assertEqual(str(e.exception), "width must be > 0")

    def test_height(self):
        """Test correct height assignment."""
        for i in range(1, 20):
            r = Rectangle(1, i)
            self.assertEqual(r.height, i)

        r.height = 10
        self.assertEqual(r.height, 10)
        with self.assertRaises(TypeError) as e:
            Rectangle(1, "1")
        self.assertEqual(str(e.exception), "height must be an integer")
        with self.assertRaises(ValueError) as e:
            Rectangle(1, 0)
        self.assertEqual(str(e.exception), "height must be > 0")

    def test_x(self):
        """Test correct x coordinate assignment."""
        for i in range(0, 20):
            r = Rectangle(1, 1, i)
            self.assertEqual(r.x, i)

        r.x = 5
        self.assertEqual(r.x, 5)
        with self.assertRaises(TypeError) as e:
            Rectangle(1, 1, "1")
        self.assertEqual(str(e.exception), "x must be an integer")
        with self.assertRaises(ValueError) as e:
            Rectangle(1, 1, -1)
        self.assertEqual(str(e.exception), "x must be >= 0")

    def test_y(self):
        """Test correct y coordinate assignment."""
        for i in range(0, 20):
            r = Rectangle(1, 1, 0, i)
            self.assertEqual(r.y, i)

        r.y = 6
        self.assertEqual(r.y, 6)
        with self.assertRaises(TypeError) as e:
            Rectangle(1, 1, 1, "1")
        self.assertEqual(str(e.exception), "y must be an integer")
        with self.assertRaises(ValueError) as e:
            Rectangle(1, 1, 1, -1)
        self.assertEqual(str(e.exception), "y must be >= 0")

    def test_area(self):
        """Test correct area calculation."""
        for i in range(1, 20):
            r = Rectangle(i, i)
            self.assertEqual(r.area(), i * i)

    def test_display(self):
        """Test correct display."""
        import sys
        import io

        f = io.StringIO()
        sys.stdout = f
        Rectangle(2, 2).display()
        self.assertEqual(f.getvalue(), "##\n##\n")

        f = io.StringIO()
        sys.stdout = f
        Rectangle(4, 4).display()
        self.assertEqual(f.getvalue(), "####\n####\n####\n####\n")

        f = io.StringIO()
        sys.stdout = f
        Rectangle(2, 3, 2, 2).display()
        self.assertEqual(f.getvalue(), "\n\n  ##\n  ##\n  ##\n")

        f = io.StringIO()
        sys.stdout = f
        Rectangle(3, 2, 1).display()
        self.assertEqual(f.getvalue(), " ###\n ###\n")

        sys.stdout = sys.__stdout__
        f.close()

    def test_str(self):
        """Test correct string representation."""
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r), "[Rectangle] (12) 2/1 - 4/6")
        r = Rectangle(5, 5, 1)
        self.assertEqual(str(r), "[Rectangle] (1) 1/0 - 5/5")
        r = Rectangle(2, 2)
        self.assertEqual(str(r), "[Rectangle] (2) 0/0 - 2/2")
