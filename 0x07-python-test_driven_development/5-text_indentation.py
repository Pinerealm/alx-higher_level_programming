#!/usr/bin/python3
"""This module contains the text_indentation function"""


def text_indentation(text=""):
    """Prints a text with 2 new lines after certain characters

    These characters are: '.', '?' and ':'

    Args:
        text (str): The text to print

    Raises:
        TypeError: If text is not a string
    """
    if not text:
        raise TypeError("no text input")
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    while i < len(text):
        if text[i] in ".?:":
            print(text[i] + "\n")
            while i < len(text) - 1 and text[i + 1] in " \t":
                i += 1
            i += 1
        else:
            print(text[i], end="")
            i += 1
