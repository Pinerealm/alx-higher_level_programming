#!/usr/bin/python3
"""This module contains the text_indentation function"""


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
    for i in range(len(text)):
        if text[i] == ' ' and text[i - 1] in '.?:':
            continue
        print(text[i], end="")
        if text[i] in ".?:":
            print("\n")
