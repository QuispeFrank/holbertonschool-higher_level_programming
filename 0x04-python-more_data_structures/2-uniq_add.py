#!/usr/bin/python3
""" Unique addition """


def uniq_add(my_list=[]):
    """ adds all unique integers in a list
        (only once for each integer)
    """
    return sum(set(my_list))
