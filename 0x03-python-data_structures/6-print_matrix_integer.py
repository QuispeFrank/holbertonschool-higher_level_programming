#!/usr/bin/python3
""" Lists of lists = Matrix """


def print_matrix_integer(matrix=[[]]):
    """ prints a matrix of integers """
    if isinstance(matrix, list):
        for row in matrix:
            print(' '.join(map(lambda e: ascii(e), row)))
