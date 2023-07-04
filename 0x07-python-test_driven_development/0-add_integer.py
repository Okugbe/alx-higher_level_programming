#!/usr/bin/python3
"""

This module has one function that adds up 2 integers

"""

def add_integer(a, b=98):
    """Return the sum of two integers or floats as an integer.

    Args:
        a (int or float): The first argument.
        b (int or float): The second argument. Default is 98.

    Returns:
        int: The sum of the two arguments as an integer.

    Raises:
        TypeError: If either of the arguments is not an integer or a float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer or a float")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer or a float")

    return int(a) + int(b)

