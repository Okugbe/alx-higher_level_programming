#!/usr/bin/python3
"""

This module contains a function that indents texts

"""


def text_indentation(text):
    """This function prints a text with 2 new lines after each ".", "?", or ":"

    Args:
        text (str): The string to be printed

    Raises:
        TypeError: If text is not a string

    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for delimiter in ".:?":
        text = (delimiter + "\n\n").join(
            [line.strip(" ") for line in text.split(delimiter)])

    print(f"{text}", end="")
