#!/usr/bin/python3
"""A rectangle is here"""


class Rectangle:
    """I'm a rectangle class.

        Attributes:
            number_of_instances: number of rectangles were
            created.
    """
    number_of_instances = 0
    print_symbol = '#'

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
        type(self).number_of_instances += 1

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
        if (self.__width * self.__height) != 0:
            return (2 * (self.__height + self.__width))
        else:
            return 0

    def __str__(self):
        """ return a string representation of the rectangle
            with the character '#'
        """
        if self.__height * self.__width != 0:
            symbol = str(self.print_symbol)
            return ((symbol * self.__width + '\n') * self.__height)[:-1]
        else:
            return ''

    def __repr__(self):
        """ return a string representation of the
            rectangle to be able to recreate a new instance
            by using eval()
        """
        return (f'Rectangle({self.__width}, {self.__height})')

    def __del__(self):
        """ destroys the rectangle :c """
        print('Bye rectangle...')
        type(self).number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ returns the biggest rectangle based on the area """
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
