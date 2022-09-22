#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""This module contains a class called Square that defines a square."""


class Square:
    """This is the Square class definition."""

    def __init__(self, size=0, position=(0, 0)):
        """__init__ method to initialize the size attribute.

        Args:
            size (int): Size of the square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        if not isinstance(position, tuple) or len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(position[0], int) or position[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(position[1], int) or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__size = size
        self.__position = position

    def area(self):
        """Calculate the area of the square.

        Returns:
            The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """Print the square with the character #."""
        if self.__size == 0:
            print()
        else:
            try:
                for i in range(self.__position[1]):
                    print()
                for i in range(self.__size):
                    print(" " * self.__position[0], end="")
                    print("#" * self.__size)
            except TypeError:
                print("position must be a tuple of 2 positive integers")

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
        if isinstance(value, int) is False:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Getter method for the position attribute.

        Returns:
            The position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Setter method for the position attribute.

        Args:
            value (:obj:`tuple` of :obj:`int`): Position of the square.
        """
        if isinstance(value, tuple) is False or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if isinstance(value[0], int) is False or value[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        if isinstance(value[1], int) is False or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
