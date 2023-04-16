#!/usr/bin/python3
"""The Base module"""
import json


class Base:
    """This defines the Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Runs on instantiation of a Base object"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of a list of dictionaries
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Returns a list of dictionaries from the JSON string representation.
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of a list of objects
        to a file
        """
        if list_objs is None:
            list_objs = []
        with open("{}.json".format(cls.__name__), "w") as f:
            f.write(cls.to_json_string(
                [o.to_dictionary() for o in list_objs]))
