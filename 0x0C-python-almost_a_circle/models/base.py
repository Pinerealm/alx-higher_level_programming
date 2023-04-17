#!/usr/bin/python3
"""The Base module"""
import json
import csv
from os import path


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

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances"""
        if not path.exists("{}.json".format(cls.__name__)):
            return []
        with open("{}.json".format(cls.__name__), "r") as f:
            o_list = cls.from_json_string(f.read())
            return [cls.create(**o_dict) for o_dict in o_list]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Writes the CSV string representation of a list of objects
        to a file
        """
        if list_objs is None:
            list_objs = []
        with open("{}.csv".format(cls.__name__), "w",) as f:
            writer = csv.writer(f)
            for o in list_objs:
                writer.writerow(o.to_dictionary().values())

    @classmethod
    def load_from_file_csv(cls):
        """Returns a list of instances from a CSV file"""
        if cls.__name__ == 'Rectangle':
            attributes = ['id', 'width', 'height', 'x', 'y']
        elif cls.__name__ == 'Square':
            attributes = ['id', 'size', 'x', 'y']

        if not path.exists("{}.csv".format(cls.__name__)):
            return []
        with open("{}.csv".format(cls.__name__), "r") as f:
            reader = csv.reader(f)
            o_list = [list(map(int, row)) for row in reader]
            return [cls.create(**dict(zip(attributes, o))) for o in o_list]
