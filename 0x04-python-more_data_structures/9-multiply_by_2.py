#!/usr/bin/python3
""" Multiply by 2 """


def multiply_by_2(a_dictionary):
    """ returns a new dictionary with all values multiplied by 2 """
    return dict((k, v * 2) for (k, v) in a_dictionary.items())
