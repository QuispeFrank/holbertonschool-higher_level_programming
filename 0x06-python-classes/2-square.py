#!/usr/bin/python3
"""A square is here"""


class Square:
    """I'm a square class.

    Attributes:
        __size: square side size.
    """

    def __init__(self, size=0):
        """Inits Square with size."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
