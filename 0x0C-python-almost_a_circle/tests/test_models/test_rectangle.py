#!/usr/bin/python3
""" Unit test for the Rectangle class """

import unittest
import json
import sys
import os
import pep8
from io import StringIO
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestRectangle(unittest.TestCase):
    """ Test cases for the Rectangle class """

    def setUp(self):
        """ Redirect the stdout to check the output of
            functions that prints.
        """
        sys.stdout = StringIO()

    def tearDown(self):
        """ Reset the nb_objects and clean everything.
        """
        Base._Base__nb_objects = 0
        sys.stdout = sys.__stdout__

    def test_pep8_conformance_model(self):
        """ Test that we conform to PEP8. """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/rectangle.py'])
        self.assertEqual(result.total_errors, 0, 'Fix pep8')

    def test_docstring(self):
        """ Testing docstring """
        self.assertIsNotNone(Rectangle.__doc__)

    def test_documentation(self):
        """ Test to see if documentation is correct
            and created.
        """
        self.assertTrue(hasattr(Rectangle, '__init__'))
        self.assertTrue(Rectangle.__init__.__doc__)
        self.assertTrue(hasattr(Rectangle, 'to_json_string'))
        self.assertTrue(Rectangle.to_json_string.__doc__)
        self.assertTrue(hasattr(Rectangle, 'from_json_string'))
        self.assertTrue(Rectangle.from_json_string.__doc__)

    def test_rectangle_id(self):
        """ Testing the id of the new rectangle """
        Base._Base__nb_objects = 0
        r = Rectangle(5, 6)
        r1 = Rectangle(4, 3, 5)
        r2 = Rectangle(1, 2, 3, 4)
        r3 = Rectangle(10, 2, 0, 0, 12)
        r4 = Rectangle(7, 8, 9, 10, 11)
        r5 = Rectangle(7, 8, 9, 10, -10)
        self.assertEqual(r.id, 1)
        self.assertEqual(r1.id, 2)
        self.assertEqual(r2.id, 3)
        self.assertEqual(r3.id, 12)
        self.assertEqual(r4.id, 11)
        self.assertEqual(r5.id, -10)

    def test_rectangle_arguments(self):
        """ Testing the number of arguments send. """
        with self.assertRaises(TypeError):
            Rectangle(10)
            Rectangle()
            Rectangle(x=10, y=11)

    def test_rectangle_TypeError_width(self):
        """ Testing the TypeError with the width
            arguments.
        """
        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            Rectangle('Holberton', 2)
            Rectangle(True, 1)
            Rectangle([1, 2, 3], 2)
            Rectangle({'x': 1, 'y': 3}, 2)
            Rectangle((4, 2), 2)
            Rectangle(None, 2)
            Rectangle(float('nan'), 2)
            Rectangle(float('inf'), 2)

    def test_rectangle_TypeError_height(self):
        """ Testing the TypeError with the height
            argument.
        """
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, 'Holberton')
            Rectangle(1, True)
            Rectangle(2, [1, 2, 3])
            Rectangle(2, {'x': 1, 'y': 3})
            Rectangle(2, (4, 2))
            Rectangle(2, None)
            Rectangle(2, float('nan'))
            Rectangle(2, float('inf'))

    def test_rectangle_TypeError_x(self):
        """ Testing the TypeError with the x argument """
        with self.assertRaisesRegex(TypeError, 'x must be an integer'):
            Rectangle(2, 3, 'Holberton')
            Rectangle(1, 3, True)
            Rectangle(2, 3, [1, 2, 3])
            Rectangle(2, 3, {'x': 1, 'y': 3})
            Rectangle(2, 3, (4, 2))
            Rectangle(2, 3, None)
            Rectangle(2, 3, float('nan'))
            Rectangle(2, 3, float('inf'))

    def test_rectangle_TypeError_y(self):
        """ Testing the TypeError with the y argument """
        with self.assertRaisesRegex(TypeError, 'y must be an integer'):
            Rectangle(2, 3, 4, 'Holberton')
            Rectangle(1, 3, 4, True)
            Rectangle(2, 3, 4, [1, 2, 3])
            Rectangle(2, 3, 4, {'x': 1, 'y': 3})
            Rectangle(2, 3, 4, (4, 2))
            Rectangle(2, 3, 4, None)
            Rectangle(2, 3, 4, float('nan'))
            Rectangle(2, 3, 4, float('inf'))

    def test_rectangle_ValueError_width(self):
        """ Testing the ValueError with the width argument """
        with self.assertRaisesRegex(ValueError, 'width must be > 0'):
            Rectangle(-10, 2)
            Rectangle(0, 2)
            Rectangle(height=2)

    def test_rectangle_ValueError_height(self):
        """ Testing the ValueError with the height argument """
        with self.assertRaisesRegex(ValueError, 'height must be > 0'):
            Rectangle(10, -2)
            Rectangle(10, 0)
            Rectangle(width=2)

    def test_rectangle_ValueError_x(self):
        """ Testing the ValueError with the x argument """
        with self.assertRaisesRegex(ValueError, 'x must be >= 0'):
            Rectangle(10, 2, -1)
            Rectangle(10, 2, -100)
            Rectangle(10, 2, 0)

    def test_rectangle_ValueError_y(self):
        """ Testing the ValueError with the y argument """
        with self.assertRaisesRegex(ValueError, 'y must be >= 0'):
            Rectangle(10, 2, 1, -2)
            Rectangle(10, 2, 100, -200)
            Rectangle(10, 2, 1, 0)

    def test_rectangle_area(self):
        """ Testing the area method """
        r = Rectangle(1, 2)
        r1 = Rectangle(3, 4, 5)
        r2 = Rectangle(6, 7, 8, 9)
        r3 = Rectangle(10, 11, 12, 13, 14)
        r4 = Rectangle(9999999999999, 9999999999999)
        self.assertEqual(r.area(), 2)
        self.assertEqual(r1.area(), 3 * 4)
        self.assertEqual(r2.area(), 6 * 7)
        self.assertEqual(r3.area(), 10 * 11)
        self.assertEqual(r4.area(), 9999999999999 * 9999999999999)

    def test_rectangle_area_args(self):
        """ Test the arguments with the method area """
        with self.assertRaises(TypeError):
            r = Rectangle()
            self.r.area(1)

    def test_rectangle_display(self):
        """ Test the output from rectangle when the
            method display is called.
        """
        r = Rectangle(2, 2)
        r1 = Rectangle(2, 3)
        r_out = '##\n' \
                '##\n'
        r1_out = '##\n' \
                 '##\n' \
                 '##\n'
        try:
            r.display()
            self.assertEqual(sys.stdout.getvalue(), r_out)
        finally:
            sys.stdout.seek(0)
            sys.stdout.truncate(0)
        try:
            r1.display()
            self.assertEqual(sys.stdout.getvalue(), r1_out)
        finally:
            sys.stdout.seek(0)
            sys.stdout.truncate(0)

    def test_rectangle_str(self):
        """ Test the __str__ method to print the Rectangle
        """
        r = Rectangle(2, 3, 2)
        self.assertEqual(r.__str__(), '[Rectangle] (1) 2/0 - 2/3')
        r1 = Rectangle(4, 5, 6, 7, 8)
        self.assertEqual(r1.__str__(), '[Rectangle] (8) 6/7 - 4/5')

    def test_rectangle_display_xy(self):
        """ Testing the display method with x and y positions
        """
        r = Rectangle(2, 3, 2, 2)
        r_out = '\n' \
                '\n' \
                '  ##\n' \
                '  ##\n' \
                '  ##\n'
        r1 = Rectangle(3, 4, 1)
        r1_out = ' ###\n' \
                 ' ###\n' \
                 ' ###\n' \
                 ' ###\n'
        try:
            r.display()
            self.assertEqual(sys.stdout.getvalue(), r_out)
        finally:
            sys.stdout.seek(0)
            sys.stdout.truncate(0)
        try:
            r1.display()
            self.assertEqual(sys.stdout.getvalue(), r1_out)
        finally:
            sys.stdout.seek(0)
            sys.stdout.truncate(0)

    def test_rectangle_update(self):
        """ Test to update a rectangle with *args """
        r = Rectangle(5, 5, 5, 5)
        self.assertEqual(r.__str__(), '[Rectangle] (1) 5/5 - 5/5')
        r.update(8)
        self.assertEqual(r.id, 8)
        self.assertEqual(r.__str__(), '[Rectangle] (8) 5/5 - 5/5')
        r.update(width=10)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.__str__(), '[Rectangle] (8) 5/5 - 10/5')
        r.update(height=6)
        self.assertEqual(r.height, 6)
        self.assertEqual(r.__str__(), '[Rectangle] (8) 5/5 - 10/6')
        r.update(x=2)
        self.assertEqual(r.x, 2)
        self.assertEqual(r.__str__(), '[Rectangle] (8) 2/5 - 10/6')
        r.update(y=3)
        self.assertEqual(r.y, 3)
        self.assertEqual(r.__str__(), '[Rectangle] (8) 2/3 - 10/6')
        r1 = Rectangle(5, 5, 5, 5)
        self.assertEqual(r1.__str__(), '[Rectangle] (2) 5/5 - 5/5')
        r1.update(*[10])
        self.assertEqual(r1.id, 10)
        self.assertEqual(r1.__str__(), '[Rectangle] (10) 5/5 - 5/5')
        r1.update(*[10, 9])
        self.assertEqual(r1.width, 9)
        self.assertEqual(r1.__str__(), '[Rectangle] (10) 5/5 - 9/5')
        r1.update(*[10, 9, 8])
        self.assertEqual(r1.height, 8)
        self.assertEqual(r1.__str__(), '[Rectangle] (10) 5/5 - 9/8')
        r1.update(*[10, 9, 8, 7])
        self.assertEqual(r1.x, 7)
        self.assertEqual(r1.__str__(), '[Rectangle] (10) 7/5 - 9/8')
        r1.update(*[10, 9, 8, 7, 6])
        self.assertEqual(r1.y, 6)
        self.assertEqual(r1.__str__(), '[Rectangle] (10) 7/6 - 9/8')

    def test_update_kwargs(self):
        """ Test to update a rectangle with **kwargs
        """
        r = Rectangle(1, 1, 1, 1)
        self.assertEqual(r.__str__(), '[Rectangle] (1) 1/1 - 1/1')
        r.update(**{'height': 10})
        self.assertEqual(r.__str__(), '[Rectangle] (1) 1/1 - 1/10')
        r.update(**{'width': 9, 'x': 8})
        self.assertEqual(r.__str__(), '[Rectangle] (1) 8/1 - 9/10')
        r.update(**{'y': 1, 'width': 2, 'x': 3, 'id': 89})
        self.assertEqual(r.__str__(), '[Rectangle] (89) 3/1 - 2/10')
        r.update(**{'x': 1, 'height': 2, 'y': 3, 'width': 4})
        self.assertEqual(r.__str__(), '[Rectangle] (89) 1/3 - 4/2')
        r.update(**{'wow': 3, 'hey': 'wow'})
        self.assertEqual(r.__str__(), '[Rectangle] (89) 1/3 - 4/2')
        r.update({'x': 10, 'height': 8})
        self.assertIs(type(r.id), dict)

    def test_to_dict(self):
        """ Testing to_dictionary method producing a dictionary
        """
        r = Rectangle(10, 2, 1, 9)
        self.assertEqual(r.__str__(), '[Rectangle] (1) 1/9 - 10/2')
        self.assertEqual(r.to_dictionary(), {
            'x': 1, 'y': 9, 'id': 1, 'height': 2, 'width': 10})
        self.assertIs(type(r.to_dictionary()), dict)
        r1 = Rectangle(1, 1)
        self.assertEqual(r1.__str__(), '[Rectangle] (2) 0/0 - 1/1')
        r1.update(**r.to_dictionary())
        self.assertEqual(r1.__str__(), '[Rectangle] (1) 1/9 - 10/2')
        self.assertNotEqual(r, r1)
