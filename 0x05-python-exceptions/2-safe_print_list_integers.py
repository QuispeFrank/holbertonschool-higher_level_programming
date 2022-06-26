#!/usr/bin/python3
""" Print and count integers """


def safe_print_list_integers(my_list=[], x=0):
    """ function that prints the first x elements of a list and only integers.

    Args:
        my_list: can contain any type (integer, string, etc.)
        x: represents the number of elements to access in my_list.
    """

    counter = 0
    for idx in range(x):
        try:
            print("{:d}".format(my_list[idx]), end='')
            counter += 1
        except (TypeError, ValueError):
            continue
    print('')

    return counter
