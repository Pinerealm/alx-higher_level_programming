#!/usr/bin/python3
"""This is the "2-matrix_divided" module."""


def matrix_divided(matrix, div):
    """Divide each element of a matrix by div.

    Args:
        matrix (list): a list of lists of integers or floats
        div (int or float): the divisor

    Returns:
        list: a new matrix containing the results of the division

    Raises:
        TypeError: if matrix is not a list of lists of integers or floats
        TypeError: if all matrix rows are not of the same size
        TypeError: if div is not an integer or float
        ZeroDivisionError: if div is 0
        OverflowError: if the divisor is too large
    """
    matrix_msg = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list) or len(matrix) == 0 or len(matrix[0]) == 0:
        raise TypeError(matrix_msg)
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(matrix_msg)
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        new_row = []
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError(matrix_msg)
            new_row.append(round(element / div, 2))
        new_matrix.append(new_row)

    if all([not all(row) for row in new_matrix]):
        raise OverflowError("divisor is too large")

    return new_matrix
