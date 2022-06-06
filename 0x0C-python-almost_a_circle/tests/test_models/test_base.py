#!/usr/bin/python3
""" Unit test for the Base class """

import unittest
import json
import os
import pep8
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """ Test cases for the Base class """

    def tearDown(self):
        """ Reset the nb_objects """
        Base._Base__nb_objects = 0

    def test_docstring(self):
        """ Testing docstring """
        self.assertIsNotNone(Base.__doc__)

    def test_documentation(self):
        """ Test to see if documentation is correct
            and created.
        """
        self.assertTrue(hasattr(Base, '__init__'))
        self.assertTrue(Base.__init__.__doc__)
        self.assertTrue(hasattr(Base, 'to_json_string'))
        self.assertTrue(Base.to_json_string.__doc__)
        self.assertTrue(hasattr(Base, 'from_json_string'))
        self.assertTrue(Base.from_json_string.__doc__)

    def test_rectangle_pep8_conformance(self):
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['./models/base.py'])
        self.assertEqual(result.total_errors, 0, 'Fix PEP8')

    def test_base_creation(self):
        """ Testing the creation of the base """
        b = Base()
        test = str(b)
        b1 = Base(12)
        test1 = str(b1)
        b2 = Base()
        test2 = str(b2)
        self.assertTrue(test[:29], '<models.base.Base object at ')
        self.assertTrue(b.id, 1)
        self.assertTrue(test1[:29], '<models.base.Base object at ')
        self.assertTrue(b1.id, 12)
        self.assertTrue(test2[:29], '<models.base.Base object at ')
        self.assertTrue(b2.id, 2)

    def test_base_instance(self):
        b = Base()
        self.assertIsInstance(b, Base)

    def test_base_id(self):
        """ Testing the increment of the nb_objects """
        b = Base()
        test = b.id
        b1 = Base()
        b2 = Base(id=33)
        b3 = Base(-2)
        self.assertTrue(test + 1, b1)
        self.assertTrue(b2.id, 33)
        self.assertTrue(b3.id, -2)

    def test_nb_objects(self):
        """ Test setting nb_objects private class attribute """
        b = Base(3)
        with self.assertRaises(AttributeError):
            print(b.nb_objects)
        with self.assertRaises(AttributeError):
            print(b.__nb_objects)

    def test_dictionary(self):
        """ Test if the function to_json_string is working
            with dictionaries.
        """
        r = Rectangle(10, 7, 2, 8)
        d = r.to_dictionary()
        jd = {'x': 2, 'y': 8, 'id': 1, 'height': 7, 'width': 10}
        jdictionary = Base.to_json_string([d])
        self.assertEqual(d, jd)
        self.assertEqual(type(d), dict)
        self.assertEqual(type(jdictionary), str)

    def test_to_json_string(self):
        """ Test if the static method is working for string
            to JSON conversion.
        """
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertTrue(type(Base.to_json_string(None)) is str)
        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertTrue(type(Base.to_json_string([])) is str)
        d = {'id': 7, 'width': 10, 'height': 7, 'x': 4, 'y': 8}
        d1 = {'id': 8, 'width': 2, 'height': 5, 'x': 9, 'y': 3}
        convert = Base.to_json_string([d, d1])
        self.assertTrue(type(convert) is str)
        dic = json.loads(convert)
        self.assertEqual(dic, [d, d1])

    def test_from_json_string(self):
        """ Test from json to string conversion """
        string = "[{'id': 7, 'width': 10, 'height': 7, 'x': 4, 'y': 8}, \
            {'id': 8, 'width': 2, 'height': 5, 'x': 9, 'y': 3}]"
        jsconv = Base.from_json_string(string)
        self.assertTrue(type(jsconv) is list)
        self.assertEqual(len(jsconv), 2)

    def test_from_json_string_empty_string(self):
        """ Test from json to string conversion managing
            empty strings.
        """
        self.assertEqual(Base.from_json_string(''), [])
        self.assertEqual(Base.from_json_string(None), [])

    def test_jfile_none(self):
        """ Testing with None as a list of instances """
        Rectangle.save_to_file(None)
        with open('Rectangle.json', mode='r') as nfile:
            self.assertEqual([], json.load(nfile))
        Square.save_to_file(None)
        with open('Square.json', mode='r') as nfile:
            self.assertEqual([], json.load(nfile))

    def test_jfile_empty(self):
        """ Testing with an empty list of instances """
        Rectangle.save_to_file([])
        with open('Rectangle.json', mode='r') as nfile:
            self.assertEqual([], json.load(nfile))
        Square.save_to_file([])
        with open('Square.json', mode='r') as nfile:
            self.assertEqual([], json.load(nfile))
