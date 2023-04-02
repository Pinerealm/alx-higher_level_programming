#!/usr/bin/python3
"""Module for the matrix_mul function."""


def matrix_mul(m_a, m_b):
    """Multiplies two matrices.
    
    Args:
        m_a (list): The first matrix.
        m_b (list): The second matrix.
    
    Returns:
        list: The product of the two matrices.

    Raises:
        TypeError: If m_a or m_b is not a list or list of lists.
        ValueError: If m_a or m_b is an empty list.
        TypeError: If m_a or m_b contains a non-integer or non-float element.
        TypeError: If m_a or m_b rows do not match.
        ValueError: If m_a and m_b can't be multiplied.
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not all([isinstance(row, list) for row in m_a]):
        raise TypeError("m_a must be a list of lists")
    if not all([isinstance(row, list) for row in m_b]):
        raise TypeError("m_b must be a list of lists")

    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    if not all([isinstance(num, (int, float)) for row in m_a for num in row]):
        raise TypeError("m_a should contain only integers or floats")
    if not all([isinstance(num, (int, float)) for row in m_b for num in row]):
        raise TypeError("m_b should contain only integers or floats")

    if not all([len(row) == len(m_a[0]) for row in m_a]):
        raise TypeError("each row of m_a must be of the same size")
    if not all([len(row) == len(m_b[0]) for row in m_b]):
        raise TypeError("each row of m_b must be of the same size")
    
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    result = []
    for row in m_a:
        result.append([])
        for col in zip(*m_b):
            dot_product = sum([a * b for a, b in zip(row, col)])
            result[-1].append(dot_product)

    return result
