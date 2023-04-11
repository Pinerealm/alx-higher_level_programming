#!/usr/bin/python3
"""The inherits_from module."""


def inherits_from(obj, a_class):
    """Check if obj is an instance of a class that inherited from a_class.

    Args:
        obj (object): The object to check.
        a_class (class): The class to check against.

    Returns:
        bool: True if obj is an instance of a class that inherited from
              a_class, otherwise False.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
