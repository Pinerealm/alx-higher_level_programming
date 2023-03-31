#!/usr/bin/python3
"""The 0-add_integer module."""


def add_integer(a, b=98):
    """Add two integers

    Args:
        a (int): first integer
        b (int): second integer with default value of 98

    Returns:
        int: sum of a and b

    Raises:
        TypeError: if a or b are not integers or floats
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    try:
        result = int(a) + int(b)
    except OverflowError:
        print("OverflowError: result is too large")
        return
    
    return int(result)
