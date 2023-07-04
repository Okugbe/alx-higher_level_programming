#!/usr/bin/python3
"""

This module contains a function that indents texts

"""
def text_indentation(text):
    """Prints a text with 2 new lines after each ".", "?", or ":"

    Args:
        text (str): The string to be printed.

    Raises:
        TypeError: If text is not a string.

    """

    # Validate if text is a string
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Initialize the count variable to track the position in the text
    count = 0

    # Skip leading spaces
    while count < len(text) and text[count] == " ":
        count = count + 1

    # Iterate through each character of the text
    while count < len(text):
        print(text[count], end="")  # Print the current character

        # Check if a new line should be added after ".", "?", or ":"
        if text[count] == "\n" or text[count] in ".?:":
            if text[count] in ".?:":
                print("\n")  # Print two new lines
            count = count + 1  # Move to the next character

            # Skip leading spaces after a new line
            while count < len(text) and text[count] == " ":
                count = count + 1
            continue

        count = count + 1  # Move to the next character

