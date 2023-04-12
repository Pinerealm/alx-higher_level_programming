#!/usr/bin/python3
"""The Square module"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Define a square; inherits from Rectangle"""

    def __init__(self, size):
        """Initialise a new Square

        Args:
            size (int): The size of the square
        """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """Calculate the area of a square"""
        return self.__size ** 2

    def __str__(self):
        """Returns an unofficial string representation"""
        return "[Square] {}/{}".format(self.__size, self.__size)
