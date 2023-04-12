#!/usr/bin/python3
"""The write_file module"""


def write_file(filename="", text=""):
    """Writes a string to a text file (UTF8)

    Args:
        filename (str): The name of the file to write to
        text (str): The string to write to the file

    Returns:
        The number of characters written
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
