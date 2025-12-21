#!/usr/bin/python3
"""The Student module"""


class Student:
    """Defines a student"""

    def __init__(self, first_name, last_name, age):
        """Initialises a student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Returns the dictionary representation, for JSON serialization,
        of an object
        """
        return vars(self)
