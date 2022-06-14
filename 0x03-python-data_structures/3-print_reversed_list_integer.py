#!/usr/bin/python3
""" Print a list of integers... in reverse! """


def print_reversed_list_integer(my_list=[]):
    """ prints all integers of a list, in reverse order """
    if isinstance(my_list, list):
        for index in reversed(range(len(my_list))):
            print(f'{my_list[index]}')
