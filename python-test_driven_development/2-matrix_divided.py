#!/usr/bin/python3
"""
Defines a matrix division function.
"""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix by a number.

    Args:
        matrix (list of lists of int/float): The matrix to divide.
        div (int, float): The divisor.

    Returns:
        list of lists: A new matrix with values divided by div
        and rounded to 2 decimal places.

    Raises:
        TypeError: If matrix is not a valid list of lists of numbers,
                   if rows are unequal in size, or if div is not a number.
        ZeroDivisionError: If div is equal to 0.
    """
    error_msg = "matrix must be a matrix (list of lists) of integers/floats"

    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(error_msg)

    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(error_msg)
        for elem in row:
            if type(elem) not in (int, float):
                raise TypeError(error_msg)

    row_length = len(matrix[0])
    for row in matrix:
        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")

    if type(div) not in (int, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(elem / div, 2) for elem in row] for row in matrix]
