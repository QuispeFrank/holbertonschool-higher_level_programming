#!/usr/bin/python3
""" Safe printing of an integers list """


def safe_print_integer(value):
    """ function that prints an integer with "{:d}".format().

    Args:
        value: can be any type (integer, string, etc.)
    """

    try:
        print('{:d}'.format(value))
    except (TypeError, ValueError):
        return False

    return True
