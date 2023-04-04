#!/usr/bin/python3
"""This is the LockedClass module"""


class LockedClass:
    """Defines a locked class with no class or object attribute.

    Attributes:
        __slots__ (list): list of attributes that can be added to the object
    """
    __slots__ = ['first_name']
