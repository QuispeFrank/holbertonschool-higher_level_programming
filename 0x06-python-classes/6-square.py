#!/usr/bin/python3
""" Coordinates of a square """


class Square:
    """class Square.
    """

    def __init__(self, size=0, position=(0, 0)):
        """ inits the square size.

        Args:
            size: (int) size of the square.
            position: (tuple) position where the square is.
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """returns the position where the square is.
        """
        return (self.__position)

    @position.setter
    def position(self, value):
        """set the square's position with validation.

        Args:
            value: (tuple) x, y position.
        """
        if not isinstance(
                value,
                tuple) or len(value) != 2 or not isinstance(
                value[0],
                int) or not isinstance(
                value[1],
                int) or value[0] < 0 or value[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        else:
            self.__position = value

    def my_print(self):
        """ print the square.
        """
        s, (x, y) = (self.size, self.position)
        if s == 0:
            y = 0
        print(('\n' * y + (' ' * x + '#' * s + '\n') * s)[:-1])
