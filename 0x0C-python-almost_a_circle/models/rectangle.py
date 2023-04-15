#!/usr/bin/python3
"""The Rectangle module"""
from .base import Base


class Rectangle(Base):
    """Defines the Rectangle class that inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialises a rectangle
        
        Args:
            width (int): The width of the rectangle
            height (int): The height of the rectangle
            x (int): The x coordinate of the rectangle
            y (int): The y coordinate of the rectangle
            id (int): The id of the rectangle
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Returns a rectangle's width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets a rectangle's width"""
        self.__width = value

    @property
    def height(self):
        """Returns a rectangle's height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets a rectangle's height"""
        self.__height = value

    @property
    def x(self):
        """Returns a rectangle's x coordinate"""
        return self.__x

    @x.setter
    def x(self, value):
        """Sets a rectangle's x coordinate"""
        self.__x = value

    @property
    def y(self):
        """Returns a rectangle's y coordinate"""
        return self.__y

    @y.setter
    def y(self, value):
        """Sets a rectangle's y coordinate"""
        self.__y = value
