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
