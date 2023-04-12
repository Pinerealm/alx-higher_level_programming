#!/usr/bin/python3
"""The Square module"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """The Square class: inherits from Rectangle"""

    def __init__(self, size):
        """Initialize a new square

        Args:
            size (int): The size of the square
        """
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Calculate the area of a square"""
        return self.__size ** 2
