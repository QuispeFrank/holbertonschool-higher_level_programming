#!/usr/bin/python3
""" To uppercase """


def uppercase(str):
    """ prints a string in uppercase followed by a new line """
    for c in str:
        c = chr(ord(c) - 32) if ord(c) >= 97 and ord(c) < 123 else c
        print('{}'.format(c), end='')
    print('')
