#!/usr/bin/python3
"""Module for the Rectangle class."""


class Rectangle:
    """Represents a rectangle.
    
    Attributes:
        number_of_instances (int): The number of instances of the class.
    """
    number_of_instances = 0
    

    def __init__(self, width=0, height=0):
        """Initializes a rectangle.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self._width = width
        self._height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Getter for the width of the rectangle.

        Returns:
            The width of the rectangle.
        """
        return self._width

    @width.setter
    def width(self, value):
        """Setter for the width of the rectangle.

        Args:
            value (int): The width of the rectangle.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    @property
    def height(self):
        """Getter for the height of the rectangle.

        Returns:
            The height of the rectangle.
        """
        return self._height

    @height.setter
    def height(self, value):
        """Setter for the height of the rectangle.

        Args:
            value (int): The height of the rectangle.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value

    def area(self):
        """Calculates the area of the rectangle.

        Returns:
            The area of the rectangle.
        """
        return self._width * self._height

    def perimeter(self):
        """Calculates the perimeter of the rectangle.

        Returns:
            The perimeter of the rectangle.
        """
        if self._width == 0 or self._height == 0:
            return 0
        return 2 * (self._width + self._height)

    def __str__(self):
        """Returns a string representation of the rectangle."""
        if self._width == 0 or self._height == 0:
            return ""
        return "\n".join(["#" * self._width] * self._height)

    def __repr__(self):
        """Returns a string representation of the rectangle."""
        return "Rectangle({}, {})".format(self._width, self._height)

    def __del__(self):
        """Prints a message when an instance is deleted."""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
