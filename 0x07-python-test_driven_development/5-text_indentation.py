#!/usr/bin/python3
"""

This module contains a function that indents texts

"""


def text_indentation(text):
    '''This function prints a text with 2 new lines after each ".", "?", or ":"

    Args:
        text (str): The string to be printed

    Raises:
        TypeError: If text is not a string

    '''
    def text_indentation(text):
    # Check if text is a string
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Remove leading and trailing spaces from the text
    text = text.strip()

    # Define the characters that require new lines
    new_line_chars = ['.', '?', ':']

    # Print the indented text
    indentation = ""
    for char in text:
        print(indentation + char, end="")
        if char in new_line_chars:
            print("\n\n" + indentation, end="")
            # Reset the indentation for the next line
            indentation = ""
        else:
            indentation += " "
    print()

