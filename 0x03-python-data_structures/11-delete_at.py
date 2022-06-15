#!/usr/bin/python3
""" Delete at """


def delete_at(my_list=[], idx=0):
    """ deletes the item at a specific position in a list """
    if idx in range(len(my_list)):
        del my_list[idx]
    return (my_list)
