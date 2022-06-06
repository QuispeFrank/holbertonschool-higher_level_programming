#!/usr/bin/python3
""" Class Base """
import json


class Base:
    """ Class to manage id attribute """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Constructor """
        if id is None:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns the JSON string representation """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return '[]'
        else:
            return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """ returns the list of the JSON string representation """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes the JSON string representation to a file """
        f = cls.__name__ + '.json'
        li = []
        if list_objs is not None:
            for i in list_objs:
                li.append(cls.to_dictionary(i))
        with open(f, mode='w', encoding='utf-8') as a_file:
            a_file.write(cls.to_json_string(li))
