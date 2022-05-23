#!/usr/bin/python3
"""A rectangle is here"""


class Rectangle:
    """I'm a rectangle class."""

    def __init__(self, width=0, height=0):
        """Inits the rectangle

            Note:
                width, height must be >= 0 integers
                otherwise raise TypeError or ValueError.

            args:
                width: rectangle's width.
                height:  rectangle's height.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ get/set for rectangle's width """
        return (self.__width)

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """ get/set for rectangle's height """
        return (self.__height)

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value
