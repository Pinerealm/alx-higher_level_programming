#!/usr/bin/python3
"""The MyInt module"""


class MyInt(int):
    """The MyInt class"""

    def __eq__(self, other):
        """Return True if both objects are not equal"""
        return int(self) != int(other)

    def __ne__(self, other):
        """Return True if both objects are equal"""
        return int(self) == int(other)
