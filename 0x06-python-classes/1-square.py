#!/usr/bin/python3
"""A square is here"""


class Square:
    """I'm a square class.

    Attributes:
        __size: square side size.
    """

    def __init__(self, size=None):
        """Inits Square with size."""
        if size is not None:
            self.__size = size
