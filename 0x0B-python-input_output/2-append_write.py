#!/usr/bin/python3
"""The append_write module"""


def append_write(filename="", text=""):
    """Appends a string at the end of a text file (UTF8)

    Args:
        filename (str): The name of the file
        text (str): The text to be appended

    Returns:
        The number of characters added
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
