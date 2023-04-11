#!/usr/bin/python3
"""The MyList module"""


class MyList(list):
    """This defines the MyList class inheriting from the list class.
    """
    def print_sorted(self):
        """Print the list, but sorted (ascending sort)"""
        print(sorted(self))
