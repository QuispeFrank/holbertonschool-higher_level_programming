#!/usr/bin/python3
""" There are only 3 colors, 10 digits, and 7 notes;
    it's what we do with them that's important
"""


def print_last_digit(number):
    """ prints the last digit of a number """
    print(abs(number) % 10, end='')
    return (abs(number) % 10)
