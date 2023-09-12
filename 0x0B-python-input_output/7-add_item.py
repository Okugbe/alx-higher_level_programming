#!/usr/bin/python3
"""This module adds all arguments to a Python list and save them to a file."""


import sys

if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file

    try:
        i = load_from_json_file("add_item.json")
    except FileNotFoundError:
        i = []
    i.extend(sys.argv[1:])
    save_to_json_file(i, "add_item.json")
