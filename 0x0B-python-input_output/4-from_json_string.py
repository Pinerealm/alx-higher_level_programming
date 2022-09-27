#!/usr/bin/python3
"""The from_json_string module"""
import json


def from_json_string(my_str):
    """Returns an object (Python data structure) from a JSON string
    representation"""
    return json.loads(my_str)
