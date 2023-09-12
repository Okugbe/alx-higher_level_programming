#!/usr/bin/python3

"""Read from a file"""


def read_file(filename=""):
    """Reads text from a file and prints to stdout"""
    with open(filename, "r", encoding="utf-8") as file:
        contents = file.read()
        print(contents)

