#!/usr/bin/python3
"""The Student class module"""


class Student:
    """The Student class"""

    def __init__(self, first_name, last_name, age):
        """Initializes the Student instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns the dictionary representation for JSON serialization
        of an object
        """
        if attrs is None:
            return self.__dict__
        else:
            new_dict = {key: value for key, value in self.__dict__.items()
                        if key in attrs}
            return new_dict

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance"""
        for key, value in json.items():
            self.__dict__[key] = value
