#!/usr/bin/python3
""" Update dictionary """


def update_dictionary(a_dictionary, key, value):
    """ replaces or adds key/value in a dictionary """
    a_dictionary.update({key: value})
    return a_dictionary
