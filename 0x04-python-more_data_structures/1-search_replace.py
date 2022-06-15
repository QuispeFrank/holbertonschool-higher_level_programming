#!/usr/bin/python3
""" Search and replace """


def search_replace(my_list, search, replace):
    """ replaces all occurrences of an element by another in a new list """
    return([replace if o == search else o for o in my_list])
