#!/usr/bin/python3
"""The MyInt module"""


class MyInt(int):
    """The MyInt class"""

    def __eq__(self, other):
        """The __eq__ method"""
        return int(self) != int(other)

    def __ne__(self, other):
        """The __ne__ method"""
        return int(self) == int(other)
