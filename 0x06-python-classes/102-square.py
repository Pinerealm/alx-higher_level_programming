#!/usr/bin/python3
"""This is the square module."""


class Square:
    """This class defines a square."""

    def __init__(self, size=0):
        """Initialises a square instance.

        Args:
            size (int): Size of the square.
        """
        self.size = size

    def area(self):
        """Calculate the area of a square.

        Returns:
            The area of the square.
        """
        return self.__size ** 2

    @property
    def size(self):
        """Getter method for the size attribute.

        Returns:
            The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method for the size attribute.

        Args:
            value (int): Size of the square.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def __eq__(self, other):
        """Check if the area of two squares are equal.

        Args:
            other (Square): Square to compare.

        Returns:
            True if equal, otherwise False."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Check if the area of two squares are not equal.

        Args:
            other (Square): Square to compare.

        Returns:
            True if not equal, otherwise False."""
        return self.area() != other.area()

    def __gt__(self, other):
        """Check if the area of the first square is greater than the second.

        Args:
            other (Square): Square to compare.

        Returns:
            True if greater, otherwise False."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Check if the area of the first square is greater than or equal to
        the second.

        Args:
            other (Square): Square to compare.

        Returns:
            True if greater than or equal to, otherwise False."""
        return self.area() >= other.area()

    def __lt__(self, other):
        """Check if the area of the first square is less than the second.

        Args:
            other (Square): Square to compare.

        Returns:
            True if less, otherwise False."""
        return self.area() < other.area()

    def __le__(self, other):
        """Check if the area of the first square is less than or equal to
        the second.

        Args:
            other (Square): Square to compare.

        Returns:
            True if less than or equal to, otherwise False."""
        return self.area() <= other.area()
