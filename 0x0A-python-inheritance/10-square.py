#!/usr/bin/python3
""" Class BaseGeometry """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ I'm a Square Class :D """
    def __init__(self, size):
        self.integer_validator('size', size)
        super().__init__(size, size)
