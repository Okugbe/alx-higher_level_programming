#!/usr/bin/python3
"""
This module has the function that add up two(2) integers

"""


def add_integer(a, b=98):
    """Returns the sum of two integers or floats as integers

    Args:
        param a: first number
        param b: second number

    Returns:
         Sum of the two integers

    Raises:
        TypeError: If either number is neither integer nor a float
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)

