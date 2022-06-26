#!/usr/bin/python3
""" Integers division with debug """


def safe_print_division(a, b):
    """ function that divides 2 integers and prints the result.

    Args:
        a: first integer
        b: second integer
    """
    res = None
    try:
        res = a / b
    except ZeroDivisionError:
        res = None
    finally:
        print('Inside result: {}'.format(res))

    return res
