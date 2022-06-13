#!/usr/bin/python3
""" islower """


def islower(letter):
    """ checks for lowercase character """
    if ord(letter) in range(ord('a'), ord('z') + 1):
        return True
    else:
        return False
