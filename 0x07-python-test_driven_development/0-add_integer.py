#!/usr/bin/python3
""" Integers addition module """


def add_integer(a, b=98):
    """
    Function that adds two integers.

    Args
        a: First number to be added.
        b: Second number to be added.

    Returns
        int(a) + int(b)
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return (int(a) + int(b))
