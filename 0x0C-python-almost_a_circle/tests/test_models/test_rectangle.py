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
        r = Rectangle(1, 1, 1, 1)
        self.assertEqual(str(r), "[Rectangle] (3) 1/1 - 1/1")

    def test_update(self):
        """Test correct update."""
        r = Rectangle(10, 10, 10, 10)
        r.update(89)
        self.assertEqual(str(r), "[Rectangle] (89) 10/10 - 10/10")

        r.update(89, 2)
        self.assertEqual(str(r), "[Rectangle] (89) 10/10 - 2/10")
        r.update(89, 2, 3)
        self.assertEqual(str(r), "[Rectangle] (89) 10/10 - 2/3")

        r.update(89, 2, 3, 4)
        self.assertEqual(str(r), "[Rectangle] (89) 4/10 - 2/3")
        r.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r), "[Rectangle] (89) 4/5 - 2/3")

        r.update(89, 3, 3, 5, 5, 6, 7, 8, 9, 10)
        self.assertEqual(str(r), "[Rectangle] (89) 5/5 - 3/3")
        r.update()
        self.assertEqual(str(r), "[Rectangle] (89) 5/5 - 3/3")

        r = Rectangle(10, 10, 10, 10)
        r.update(height=1)
        self.assertEqual(str(r), "[Rectangle] (2) 10/10 - 10/1")
        r.update(width=1, x=2)
        self.assertEqual(str(r), "[Rectangle] (2) 2/10 - 1/1")

        r.update(y=1, width=2, x=3, id=89)
        self.assertEqual(str(r), "[Rectangle] (89) 3/1 - 2/1")
        r.update(x=1, height=2, y=3, width=4)
        self.assertEqual(str(r), "[Rectangle] (89) 1/3 - 4/2")

        r.update(x=2, name="Holberton", height=4, y=3, width=4, id=89)
        self.assertEqual(str(r), "[Rectangle] (89) 2/3 - 4/4")

    def test_to_dictionary(self):
        """Test correct dictionary representation."""
        r1 = Rectangle(10, 2, 1, 9)
        d1 = r1.to_dictionary()
        result = {'x': 1, 'y': 9, 'id': 1, 'height': 2, 'width': 10}
        self.assertEqual(d1, result)
        self.assertIsInstance(d1, dict)

        r = Rectangle(1, 1)
        d = r.to_dictionary()
        result = {'x': 0, 'y': 0, 'id': 2, 'height': 1, 'width': 1}
        self.assertEqual(d, result)
        self.assertIsInstance(d, dict)

        r = Rectangle(5, 8, 3, 4, 9)
        d = r.to_dictionary()
        result = {'x': 3, 'y': 4, 'id': 9, 'height': 8, 'width': 5}
        self.assertEqual(d, result)
        self.assertIsInstance(d, dict)

        # Test update with dictionary
        r.update(**d1)
        self.assertEqual(str(r), "[Rectangle] (1) 1/9 - 10/2")
        self.assertNotEqual(r, r1)
