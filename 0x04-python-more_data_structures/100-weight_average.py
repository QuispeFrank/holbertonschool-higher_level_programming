#!/usr/bin/python3
""" Weighted average! """


def weight_average(my_list=[]):
    """ returns the weighted average of all integers tuple
        (<score>, <weight>)
    """
    if my_list:
        return sum(k * v for k, v in my_list) / sum(v for k, v in my_list)
