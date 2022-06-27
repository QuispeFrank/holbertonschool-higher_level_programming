#!/usr/bin/python3
""" Square with size """


class Square:
    """ class Square.
    """

    def __init__(self, size=None):
        """ inits the Square with size.

        Args:
            size: size of the square.
        """
        if size is not None:
            self.__size = size
