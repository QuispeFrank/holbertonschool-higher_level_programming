#!/usr/bin/python3
""" Simple delete by key """


def simple_delete(a_dictionary, key=""):
    """ deletes a key in a dictionary """
    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary
