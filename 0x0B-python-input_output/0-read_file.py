#!/usr/bin/python3

"""Read from a file"""


def read_file(filename=""):
    with open(filename, "r") as file:
        contents = file.read()
    return contents
