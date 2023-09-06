#!/usr/bin/python3

"""
This module divides all elements of a matrix.

"""


def matrix_divided(matrix, div):
    """This function that divides all elements of a matrix

    Args:
        matrix: A list of lists of integers or floats
        div: Number used for division must be a number (integer or float)
    Raises:
        TypeError: If the matrix contains non-numbers
        TypeError: If the row of the matrix have different sizes
        TypeError: If the div is not a number (integer or float)
        ZeroDivisionError: If div is equal to 0
    Returns:
        A new matrix which represents the result of the divisions
    """

    res_matrix = []

    if not matrix or matrix is [[]] or matrix is None:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    for i in range(len(matrix)):
        if len(matrix[i]) is not len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        res_matrix.append([])
        for n in matrix[i]:
            if type(n) is int or type(n) is float:
                res_matrix[i].append(round(n / div, 2))
            else:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    return res_matrix
