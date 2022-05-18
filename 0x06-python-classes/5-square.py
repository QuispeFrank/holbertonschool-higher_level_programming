#!/usr/bin/python3
"""A square is here"""


class Square:
    """I'm a square class."""

    def __init__(self, size=0):
        """Inits Square with size.

            args:
                __size: size of the square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property
    def size(self):
        """get/set size of the square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Returns the Square's area"""
        return (self.__size * self.__size)

    def my_print(self):
        """Prints a square"""
        for row in range(self.__size):
            for dist in range(self.__size):
                print("#", end="" if self.__size - 1 != dist else "\n")
        if self.__size == 0:
            print("")
