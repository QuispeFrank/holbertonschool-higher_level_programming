#!/usr/bin/python3
""" Squared simple """


def square_matrix_simple(matrix=[]):
    """ computes the square value of all integers of a matrix """
    return([list(map(lambda n: n ** 2, row)) for row in matrix])
