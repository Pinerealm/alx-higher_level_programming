#!/usr/bin/python3
"""This is the square module."""


class Square:
    """This class defines a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialises a square instance.

        Args:
            size (int): Size of the square.
            position (tuple): Position of the square.
        """
        self.__size = size
        self.__position = position

    def area(self):
        """Calculate the area of a square.

        Returns:
            The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """Print out the square to stdout using the character #.
    
        position[0] is the number of spaces to skip before printing the square.
        position[1] is the number of new lines to print
                    before printing the square.
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)

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
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or value[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[1], int) or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
