#!/usr/bin/python3
""""

This module contains a function that prints a name

"""


def say_my_name(first_name, last_name=""):
    '''This function prints name (<first name> <last name>)

    Args:
        first_name (str): The fisrt name to be printed
        last_name (str): The last name to be printed

    Raises:
        TypeError: If either the first_name and last_name are not strings

    '''
    def say_my_name(first_name, last_name=""):
    # Check if first_name and last_name are strings
    if not isinstance(first_name, str) or not isinstance(last_name, str):
        raise TypeError("first_name must be a string or last_name must be a string")

    # Print the formatted name
    if last_name:
        print("My name is {} {}".format(first_name, last_name))
    else:
        print("My name is {}".format(first_name))

