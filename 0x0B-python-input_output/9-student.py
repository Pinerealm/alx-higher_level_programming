#!/usr/bin/python3
"""The Student class module"""


class Student:
    """The Student class"""

    def __init__(self, first_name, last_name, age):
        """Initializes the Student instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Returns the dictionary representation for JSON serialization
        of an object
        """
        return self.__dict__
