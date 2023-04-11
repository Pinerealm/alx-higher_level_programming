#!/usr/bin/python3
"""The is_same_class module."""


def is_same_class(obj, a_class):
    """Checks if an object is an instance of a class.

    Args:
        obj (object): The object to check.
        a_class (class): The class to check against.

    Returns:
        bool: True if obj is an instance of a_class, otherwise False.
    """
    return type(obj) is a_class
