#!/usr/bin/python3
"""This is the "5-text_indentation" module."""


def text_indentation(text):
    """Prints a text with 2 new lines after certain characters

    These characters are: '.', '?' and ':'

    Args:
        text (str): The text to print

    Raises:
        TypeError: If text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    buffer = ""
    skip_spaces = True

    for char in text:
        if skip_spaces and char in " \t":
            continue
        skip_spaces = False
        buffer += char

        if char in ".?:":
            buffer += "\n\n"
            skip_spaces = True

    print(buffer, end="")
