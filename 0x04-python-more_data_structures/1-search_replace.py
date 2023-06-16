#!/usr/bin/python3

def search_replace(my_list, search, replace):
    """
    Replaces all occurrences of an element by another in a new list.
    """
    replaced_list = [replace if item == search else item for item in my_list]
    return replaced_list
