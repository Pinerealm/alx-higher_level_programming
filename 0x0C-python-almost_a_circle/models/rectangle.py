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
        """Sets a rectangle's width after validation"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Returns a rectangle's height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets a rectangle's height after validation"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Returns a rectangle's x coordinate"""
        return self.__x

    @x.setter
    def x(self, value):
        """Sets a rectangle's x coordinate after validation"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Returns a rectangle's y coordinate"""
        return self.__y

    @y.setter
    def y(self, value):
        """Sets a rectangle's y coordinate after validation"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns the area of a rectangle"""
        return self.width * self.height

    def display(self):
        """Prints a rectangle with the '#' character"""
        for i in range(self.y):
            print()
        for i in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """Returns an informal string representation of a rectangle"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """Updates a rectangle's attributes"""
        attributes = ["id", "width", "height", "x", "y"]
        if args:
            len_args = len(args) if len(args) < 5 else 5
            for i in range(len_args):
                setattr(self, attributes[i], args[i])
        else:
            for key, value in kwargs.items():
                if key in attributes:
                    setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of a rectangle"""
        return {
            "id": self.id, "width": self.width,
            "height": self.height, "x": self.x, "y": self.y
        }
