#!/usr/bin/python3
""" Tuples addition """


def add_tuple(tuple_a=(), tuple_b=()):
    """ adds 2 tuples """
    tuple_a += (0, 0)
    tuple_b += (0, 0)
    return(tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
