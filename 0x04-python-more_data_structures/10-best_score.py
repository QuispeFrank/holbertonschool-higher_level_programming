#!/usr/bin/python3
""" Best score """


def best_score(a_dictionary):
    """ returns a key with the biggest integer value """
    return max(a_dictionary, key=a_dictionary.get) if a_dictionary else None
