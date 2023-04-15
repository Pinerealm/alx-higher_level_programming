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
