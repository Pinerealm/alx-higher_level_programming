"""Unittests for the square module."""
import unittest
from models.square import Square
from models.base import Base
from models.rectangle import Rectangle


class TestSquare(unittest.TestCase):
    """Defines tests for the Square class."""

    def setUp(self):
        """Runs before each test."""
        Base._Base__nb_objects = 0

    def test_id(self):
        """Test correct id assignment after instantiation."""
        for i in range(1, 20):
            s = Square(1)
            self.assertEqual(s.id, i)

        s = Square(1, 0, 0, 12)
        self.assertEqual(s.id, 12)

        with self.assertRaises(TypeError) as e:
            Square()
        self.assertEqual(str(e.exception), "__init__() missing 1 required "
                                           "positional argument: 'size'")

    def test_size(self):
        """Test correct width assignment."""
        for i in range(1, 20):
            s = Square(i)
            self.assertEqual(s.width, i)
            self.assertEqual(s.height, i)

        s.size = 10
        self.assertEqual(s.width, 10)
        self.assertEqual(s.height, 10)
        with self.assertRaises(TypeError) as e:
            Square("1")
        self.assertEqual(str(e.exception), "width must be an integer")

        with self.assertRaises(ValueError) as e:
            Square(0)
        self.assertEqual(str(e.exception), "width must be > 0")

    def test_x(self):
        """Test correct x coordinate assignment."""
        for i in range(0, 20):
            s = Square(1, i)
            self.assertEqual(s.x, i)

        s.x = 10
        self.assertEqual(s.x, 10)
        with self.assertRaises(TypeError) as e:
            Square(1, "1")
        self.assertEqual(str(e.exception), "x must be an integer")
        with self.assertRaises(ValueError) as e:
            Square(1, -1)
        self.assertEqual(str(e.exception), "x must be >= 0")

    def test_y(self):
        """Test correct y coordinate assignment."""
        for i in range(0, 20):
            s = Square(1, 1, i)
            self.assertEqual(s.y, i)

        s.y = 10
        self.assertEqual(s.y, 10)
        with self.assertRaises(TypeError) as e:
            Square(1, 1, "1")
        self.assertEqual(str(e.exception), "y must be an integer")
        with self.assertRaises(ValueError) as e:
            Square(1, 1, -1)
        self.assertEqual(str(e.exception), "y must be >= 0")

    def test_str(self):
        """Test correct string representation."""
        s = Square(4, 2, 1, 12)
        self.assertEqual(str(s), "[Square] (12) 2/1 - 4")
        s = Square(5, 1)
        self.assertEqual(str(s), "[Square] (1) 1/0 - 5")

        s = Square(1, 1, 1, 1)
        self.assertEqual(str(s), "[Square] (1) 1/1 - 1")
        s = Square(1, 1, 1)
        self.assertEqual(str(s), "[Square] (2) 1/1 - 1")

    def test_display(self):
        """Test correct display output."""
        import sys
        from io import StringIO

        f = StringIO()
        sys.stdout = f
        Square(4).display()
        self.assertEqual(f.getvalue(), "####\n####\n####\n####\n")

        f = StringIO()
        sys.stdout = f
        Square(2, 2).display()
        self.assertEqual(f.getvalue(), "  ##\n  ##\n")

        f = StringIO()
        sys.stdout = f
        Square(2, 3, 2).display()
        self.assertEqual(f.getvalue(), "\n\n   ##\n   ##\n")

        sys.stdout = sys.__stdout__
        f.close()

    def test_update(self):
        """Test correct update"""
        s = Square(10, 10, 10)
        s.update(89)
        self.assertEqual(str(s), "[Square] (89) 10/10 - 10")
        s.update(89, 2)
        self.assertEqual(str(s), "[Square] (89) 10/10 - 2")

        s.update(89, 2, 3)
        self.assertEqual(str(s), "[Square] (89) 3/10 - 2")
        s.update(89, 2, 3, 4)
        self.assertEqual(str(s), "[Square] (89) 3/4 - 2")

        s.update(20, 4, 5, 6, 7, 8, 9, 10)
        self.assertEqual(str(s), "[Square] (20) 5/6 - 4")
        s.update()
        self.assertEqual(str(s), "[Square] (20) 5/6 - 4")

        s.update(x=1, size=4, y=3, id=15)
        self.assertEqual(str(s), "[Square] (15) 1/3 - 4")
        s.update(size=8, y=1, x=2, id=30)
        self.assertEqual(str(s), "[Square] (30) 2/1 - 8")

        s.update(y=1, name="Square", size=4, x=2, id=35)
        self.assertEqual(str(s), "[Square] (35) 2/1 - 4")
