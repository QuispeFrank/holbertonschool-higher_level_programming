#!/usr/bin/python3
""" Replace in a copy """


def new_in_list(my_list, idx, element):
    """ replaces an element in a list at a specific position
        without modifying the original list (like in C)
    """
    if isinstance(my_list, list):
        newlist = my_list.copy()
        if idx in range(0, len(my_list)):
            newlist[idx] = element
        return(newlist)
