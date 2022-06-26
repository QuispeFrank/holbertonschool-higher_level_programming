#!/usr/bin/python3
""" Safe integer print with error message """
import sys


def safe_print_integer_err(value):
    """function that prints an integer.

    Args:
        value: integer.
    """
    try:
        print("{:d}".format(value))
    except (TypeError, ValueError) as err:
        sys.stderr.write("Exception: {}\n".format(err))
        return False

    return True
