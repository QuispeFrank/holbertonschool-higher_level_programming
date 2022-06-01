#!/usr/bin/python3
""" Read file """


def read_file(filename=""):
    """ function that reads a text file (UTF8)
        and prints it to stdout.
    """
    with open(filename, mode='r', encoding='utf-8') as f:
        print(end=f.read())
