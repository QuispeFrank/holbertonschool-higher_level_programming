#!/usr/bin/python3
""" Class Rectangle """
from models.base import Base


class Rectangle(Base):
    """ Class that inherits from Base """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Constructor to initialize attr """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ get width """
        return self.__width

    @width.setter
    def width(self, width):
        """ set width """
        if type(width) is not int:
            raise TypeError('width must be an integer')
        if width <= 0:
            raise ValueError('width must be > 0')
        self.__width = width

    @property
    def height(self):
        """ get height """
        return self.__height

    @height.setter
    def height(self, height):
        """ set height """
        if type(height) is not int:
            raise TypeError('height must be an integer')
        if height <= 0:
            raise ValueError('height must be > 0')
        self.__height = height

    @property
    def x(self):
        """ get x """
        return self.__x

    @x.setter
    def x(self, x):
        """ set x """
        if type(x) is not int:
            raise TypeError('x must be an integer')
        if x < 0:
            raise ValueError('x must be >= 0')
        self.__x = x

    @property
    def y(self):
        """ get y """
        return self.__y

    @y.setter
    def y(self, y):
        """ set y """
        if type(y) is not int:
            raise TypeError('y must be an integer')
        if y < 0:
            raise ValueError('y must be >= 0')
        self.__y = y

    def area(self):
        """ area of the rectangle """
        return self.__width * self.__height

    def display(self):
        """ prints in stdout the Rectangle """
        altura = self.__height
        i = 0
        print(('\n' * self.__y), end='')
        while i < altura:
            print((' ' * self.__x), end='')
            print('#' * self.__width)
            i += 1

    def __str__(self):
        """ Magic method str to print """
        return '[Rectangle] ({}) {}/{} - {}/{}'.format(
            self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """ take args from the command line """
        if len(args):
            if args[0] is not None:
                self.id = args[0]
            if len(args) > 1:
                self.__width = args[1]
            if len(args) > 2:
                self.__height = args[2]
            if len(args) > 3:
                self.__x = args[3]
            if len(args) > 4:
                self.__y = args[4]
        else:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'width' in kwargs:
                self.__width = kwargs['width']
            if 'height' in kwargs:
                self.__height = kwargs['height']
            if 'x' in kwargs:
                self.__x = kwargs['x']
            if 'y' in kwargs:
                self.__y = kwargs['y']

    def to_dictionary(self):
        """ returns the dictionary representation """
        return {'x': self.__x, 'y': self.__y, 'id': self.id,
                'height': self.__height, 'width': self.__width}
