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

    i = 0
    text_len = len(text)
    string = ""
    while i < text_len:
        if text[i] in ".?:":
            string += text[i] + "\n\n"
            print(string, end="")
            string = ""
            while i < text_len - 1 and text[i + 1] in " \t":
                i += 1
            i += 1
        else:
            string += text[i]
            i += 1
    print(string, end="")
