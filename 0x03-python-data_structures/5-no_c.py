#!/usr/bin/python3
""" Can you C me now? """


def no_c(my_string):
    """ removes all characters c and C from a string """
    if isinstance(my_string, str):
        return(''.join(filter(lambda c: c not in 'cC', my_string)))
