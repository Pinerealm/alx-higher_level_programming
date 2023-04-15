#!/usr/bin/python3
"""The Square module"""
from .rectangle import Rectangle


class Square(Rectangle):
    """Defines the Square class that inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialises a square

        Args:
            size (int): The size of the square
            x (int): The x coordinate of the square
            y (int): The y coordinate of the square
            id (int): The id of the square
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Returns the size of a square"""
        return self.width

    @size.setter
    def size(self, value):
        """Sets the size of a square"""
        self.width = value
        self.height = value

    def __str__(self):
        """Returns an informal string representation of a square"""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)
