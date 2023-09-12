#!/usr/bin/python3

"""Pascal's Triangle"""


def pascal_triangle(n):
    """
    returns a list of lists of integers representing the Pascal’s triangle of n
    Returns an empty list if n <= 0
    You can assume n will be always an integer
    """
    triangle = []
    if n <= 0:
        return triangle
    if n == 0:
        return [[1]]

    triangle = [[1]]
    for item in range(n-1):
        triangle.append([a+b for a, b in zip([0] + triangle[-1], triangle[-1] + [0])])
    return triangle
