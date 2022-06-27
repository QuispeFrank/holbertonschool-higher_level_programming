#!/usr/bin/python3
"""A square is here"""


class Square:
    """class Square.
    """

    def __init__(self, size=0):
        """ inits the square size.

        Args:
            size: (int) size of the square.
        """
        self.size = size

    def area(self):
        """area of the square.
        """
        return (self.__size * self.__size)

    @property
    def size(self):
        """ returns square's size.
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """ set the square's size with validation.

        Args:
            value: square's size.
        """
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value
