#!/usr/bin/python3
"""The class_to_json module"""


def class_to_json(obj):
    """Returns the dictionary description, for JSON serialization,
    of an object
    """
    return vars(obj)
