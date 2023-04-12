#!/usr/bin/python3
"""The Rectangle module"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Defines a rectangle; inherits from BaseGeometry"""

    def __init__(self, width, height):
        """Initialise a new Rectangle

        Args:
            width (int): The width of the rectangle
            height (int): The height of the rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Calculate the area of a rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Returns an unofficial string representation"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
