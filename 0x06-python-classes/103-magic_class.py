#!/usr/bin/python3
"""This is the MagicClass module."""
import math


class MagicClass:
    """This class defines a circle."""

    def __init__(self, radius=0):
        """Initialise a MagicClass instance.

        Args:
            radius (int): Radius of the circle.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Calculate the area of a circle.

        Returns:
            The area of the circle.
        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Calculate the circumference of a circle.

        Returns:
            The circumference of the circle.
        """
        return 2 * math.pi * self.__radius
