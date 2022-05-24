#!/usr/bin/python3
"""A rectangle is here"""


class Rectangle:
    """I'm a rectangle class."""

    def __init__(self, width=0, height=0):
        """Inits the rectangle

        Note:
            width, height must be >= 0 integers
            otherwise raise TypeError or ValueError.

        args
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

    def area(self):
        """ Returns the rectangle's area """
        return (self.__height * self.__width)

    def perimeter(self):
        """ Returns the rectangle's perimeter """
        if (self.__width * self.__height != 0):
            return (2 * (self.__height + self.__width))
        else:
            return 0
    
    def __str__(self):
        """ prints # """
        if self.__height * self.__width != 0:
            return (('#' * self.__width + '\n') * self.__height)[:-1]
        else:
            return ""
