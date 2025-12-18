#!/usr/bin/python3
"""Module for the Rectangle class."""


class Rectangle:
    """Represents a rectangle.

    Attributes:
        number_of_instances (int): The number of existing rectangles.
    """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initializes a rectangle.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Gets the width of the rectangle.

        Returns:
            The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle.

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
        self.__width = value

    @property
    def height(self):
        """Gets the height of the rectangle.

        Returns:
            The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle.

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
        self.__height = value

    def area(self):
        """Calculates the area of a rectangle.

        Returns:
            The area of the rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """Calculates the perimeter of a rectangle.

        Returns:
            The perimeter of the rectangle.
        """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """Returns the unofficial string representation of the rectangle.
        """
        if self.width == 0 or self.height == 0:
            return ""
        return "\n".join(["#" * self.width] * self.height)

    def __repr__(self):
        """Returns the official representation of a rectangle.
        """
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """Prints a message when an instance is deleted."""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
