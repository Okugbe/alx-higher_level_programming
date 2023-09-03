#!/usr/bin/python3
"""

This module contain a function that prints a square

"""


def print_square(size):
    """This function prints a square with the character #

    Args:
        size (int): This represents the length of the square

    Raises:
        TypeError: If size is not an integer
        TypeError: If size is a float and less than zero
        ValueError: If size is less than zero

    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) or size < 0:
        raise TypeError("size must be an integer")

    for l in range(0, size):
        for b in range(size):
            print("#", end="")
        print("")
