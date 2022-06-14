#!/usr/bin/python3
""" Replace element """


def replace_in_list(my_list, idx, element):
    """ replaces an element of a list at a
        specific position (like in C)
    """
    if idx in range(0, len(my_list)):
        my_list[idx] = element
    return(my_list)
