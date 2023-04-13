#!/usr/bin/python3
"""The append_after module"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts a line of text into a file after each line containing
    a specific string

    Args:
        filename (str): The name of the file to be modified
        search_string (str): The string to search for
        new_string (str): The string to insert after each line containing
        search_string
    """
    with open(filename, mode="r", encoding="utf-8") as f:
        lines = f.readlines()
    with open(filename, mode="w", encoding="utf-8") as f:
        for line in lines:
            f.write(line)
            if search_string in line:
                f.write(new_string)
