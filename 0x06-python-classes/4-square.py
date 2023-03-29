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
