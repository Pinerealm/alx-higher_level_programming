#!/usr/bin/python3
"""This module contains a function that prints a name passed to it"""


def say_my_name(first_name, last_name=""):
    """Prints a name passed to it

    Args:
        first_name (str): The first name
        last_name (str): The last name

    Raises:
        TypeError: If first_name or last_name is not a string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    if last_name == "" and first_name == "":
        raise TypeError("no name given")

    print("My name is {} {}".format(first_name, last_name))
