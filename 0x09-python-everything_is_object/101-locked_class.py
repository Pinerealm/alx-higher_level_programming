#!/usr/bin/python3
"""The locked class module"""


class LockedClass:
    """The locked class"""
    __slots__ = ["first_name"]
    
    def __init__(self, first_name=""):
        """The locked class constructor"""
        self.first_name = first_name
