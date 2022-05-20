#!/usr/bin/python3
"""A square is here"""


class Square:
    """I'm a square class."""

    def __init__(self, size=0, position=(0, 0)):
        """Inits Square with size.

            args:
                __size: size of the square.
                __position: 2D position where the square is.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

        if not isinstance(position[0] * position[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(position) != 2 or position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

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

    @property
    def position(self):
        """get/set position of the square"""
        return (self.__position)

    @position.setter
    def position(self, value):
        if len(value) != 2 or value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Returns the Square's area"""
        return (self.__size * self.__size)

    def my_print(self):
        """Prints a square"""
        [print("") for pos_y in range(self.__position[1])]
        for row in range(self.__size):
            [print(end=" ") for pos_x in range(self.__position[0])]
            [print(end="#") for col in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
