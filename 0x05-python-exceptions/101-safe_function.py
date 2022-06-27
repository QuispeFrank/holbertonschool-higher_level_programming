#!/usr/bin/python3
""" Safe integer print with error message """
import sys


def safe_function(fct, *args):
    """function that executes a function safely.

    Args:
        fct: a pointer to a function.
        args: function's args.
    """
    try:
        return(fct(*args))
    except BaseException as err:
        sys.stderr.write(f'Exception: {err}\n')
        return None
