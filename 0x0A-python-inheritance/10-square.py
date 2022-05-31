#!/usr/bin/python3
""" Class BaseGeometry """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ I'm a Square Class :D """
    def __init__(self, lado):
        self.integer_validator('lado', lado)
        super().__init__(lado, lado)
        self.__lado = lado

    def area(self):
        return (self.__lado * self.__lado)
