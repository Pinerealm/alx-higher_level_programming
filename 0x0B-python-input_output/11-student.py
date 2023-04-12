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
        if attrs is None:
            return self.__dict__
        else:
            new_dict = {key: value for key, value in self.__dict__.items()
                        if key in attrs}
            return new_dict

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance
        
        Args:
            json (dict): A dictionary of attributes to replace
        """
        for key, value in json.items():
            self.__dict__[key] = value
