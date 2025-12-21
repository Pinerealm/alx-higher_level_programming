#!/usr/bin/python3
"""The Student module"""


class Student:
    """Defines a student"""

    def __init__(self, first_name, last_name, age):
        """Initialises a student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Get a dictionary representation of a Student instance

        Args:
            attrs (list): A list of attributes to retrieve

        Returns:
            A dictionary representation of a Student instance
        """
        obj_dict = vars(self)
        if attrs is None:
            return obj_dict
        else:
            return {
                key: val for key, val in obj_dict.items()
                if key in attrs
            }

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance

        Args:
            json (dict): A dictionary of attributes to replace
        """
        for key, value in json.items():
            setattr(self, key, value)
