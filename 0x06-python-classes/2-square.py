#!/usr/bin/python3
"""This is the square module."""


class Square:
    """This class defines a square."""

    def __init__(self, size=0):
        """Initialises a square instance.

        Args:
            size (int): Size of the square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
