#!/usr/bin/python3

def best_score(a_dictionary):
    """
    Returns the key with the biggest integer value from a dictionary.
    If no score found, returns None.
    """

    return max(a_dictionary, key=a_dictionary.get) if a_dictionary else None
