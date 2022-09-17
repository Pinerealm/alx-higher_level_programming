#!/usr/bin/python3
"""This module contains a function that divides all elements of a matrix"""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix

    Args:
        matrix (list): a list of lists of integers or floats
        div (int or float): the divisor

    Returns:
        list: a new matrix where each element is divided by div

    Raises:
        TypeError: if matrix is not a list of lists
        TypeError: if matrix contains non-integer or non-float elements
        TypeError: if div is not an integer or float
        ZeroDivisionError: if div is 0
    """
    if isinstance(matrix, list) is False:
        raise TypeError("matrix must be a matrix (list of lists)"
                        " of integers/floats")
    if isinstance(matrix[0], list) is False:
        raise TypeError("matrix must be a matrix (list of lists)"
                        " of integers/floats")
    if isinstance(div, (int, float)) is False:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = []
    for row in matrix:
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        new_row = []
        for element in row:
            if isinstance(element, (int, float)) is False:
                raise TypeError("matrix must be a matrix (list of lists)"
                                " of integers/floats")
            new_row.append(round(element / div, 2))
        new_matrix.append(new_row)
    return new_matrix
