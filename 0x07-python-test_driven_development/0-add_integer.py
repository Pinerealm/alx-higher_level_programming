#!/usr/bin/python3
"""This module contains a function that adds two integers"""


def add_integer(a, b=98):
    """Add two integers

    Args:
        a (int): first integer
        b (int): second integer

    Returns:
        int: sum of a and b

    Raises:
        TypeError: if a or b are not integers
    """
    if isinstance(a, (int, float)) is False:
        raise TypeError("a must be an integer")
    if isinstance(b, (int, float)) is False:
        raise TypeError("b must be an integer")

    result = a + b
    if result == float('inf') or result == float('-inf'):
        raise OverflowError("result is too large")

    return int(a) + int(b)
