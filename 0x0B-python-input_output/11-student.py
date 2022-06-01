#!/usr/bin/python3
""" Student to JSON """


class Student():
    """ I'm a student class :) """
    def __init__(self, first_name, last_name, age):
        """ inits a student """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ F. that returns student's information """
        if type(attrs) != list:
            return self.__dict__
        d = {k: v for k, v in self.__dict__.items() for a in attrs if a == k}
        return (d)

    def reload_from_json(self, json):
        """ updates the dictionary """
        self.__dict__.update(json)
