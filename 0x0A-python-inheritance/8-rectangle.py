#!/usr/bin/python3
""" Class BaseGeometry """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ I'm a BaseGeometry class :D """
    def __init__(self, width, height):
        self.integer_validator('width', width)
        self.integer_validator('height', height)
