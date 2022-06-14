#!/usr/bin/python3
""" Find the max """


def max_integer(my_list=[]):
    """ finds the biggest integer of a list """
    return(sorted(my_list)[-1] if my_list else None)
