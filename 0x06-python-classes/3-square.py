#!/usr/bin/python3
"""This is the square module"""


class Square:
    """This class defines a square."""

    def __init__(self, size=0):
        """Initialises a square instance.

        Args:
            size (int): Size of the square.
        """
        if isinstance(size, int) is False:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Calculate the area of a square.

        Returns:
            The area of the square.
        """
        return self.__size ** 2
