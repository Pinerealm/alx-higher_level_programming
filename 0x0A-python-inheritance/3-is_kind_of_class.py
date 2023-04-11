#!/usr/bin/python3
"""The is_kind_of_class module."""


def is_kind_of_class(obj, a_class):
    """Checks if obj is an instance of a_class or a subclass of a_class.

    Args:
        obj (object): The object to check.
        a_class (class): The class to check against.

    Returns:
        bool: True if obj is an instance of a_class or a subclass of a_class,
              otherwise False.
    """
    return isinstance(obj, a_class)
