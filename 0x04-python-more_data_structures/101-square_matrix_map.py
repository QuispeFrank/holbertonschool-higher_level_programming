#!/usr/bin/python3
""" Squared by using map """


def square_matrix_map(matrix=[]):
    """ computes the square value of all integers of a matrix using map """
    return list(map(lambda row: list(map(lambda n: n ** 2, row)), matrix))
