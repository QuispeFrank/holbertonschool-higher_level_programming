#!/usr/bin/python3
""" Secure access to an element in a list """


def element_at(my_list, idx):
    """ retrieves an element from a list like in C """
    return(my_list[idx] if idx in range(0, len(my_list)) else None)
