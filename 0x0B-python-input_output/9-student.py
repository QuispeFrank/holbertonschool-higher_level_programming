#!/usr/bin/python3
""" Student to JSON """


class Student():
    """ I'm a student class :) """
    def __init__(self, first_name, last_name, age):
        """ inits a student """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ F. that returns student's information """
        return (self.__dict__)
