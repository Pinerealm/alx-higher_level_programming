#!/usr/bin/python3
"""The add_attribute module"""


def add_attribute(obj, name, value):
    """The add_attribute function

    Args:
        obj: The object to add the attribute to
        name: The name of the attribute
        value: The value of the attribute

    Raises:
        TypeError: If adding  the attribute is not possible
    """
    if hasattr(obj, "__dict__"):
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")
