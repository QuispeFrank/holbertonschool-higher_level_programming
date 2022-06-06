#!/usr/bin/python3
""" Class Square """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Class square that inherits from rectangle """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """ get size """
        return self.width

    @size.setter
    def size(self, size):
        """ set size """
        self.width = size
        self.height = size

    def __str__(self):
        """ Magic method str to print """
        return '[Square] ({}) {}/{} - {}'.format(
            self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""
        if len(args):
            if args[0] is not None:
                self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        else:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'size' in kwargs:
                self.size = kwargs['size']
            if 'x' in kwargs:
                self.x = kwargs['x']
            if 'y' in kwargs:
                self.y = kwargs['y']

    def to_dictionary(self):
        """returns the dictionary representation of a Square"""
        return {'id': self.id, 'size': self.width, 'x': self.x, 'y': self.y}
