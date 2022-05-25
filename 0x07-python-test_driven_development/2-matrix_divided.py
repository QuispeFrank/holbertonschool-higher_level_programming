#!/usr/bin/python3
""" Divide a matrix module """


def matrix_divided(matrix, div):
    """ divides all elements of a matrix. """

    """ error messages """
    typerror = 'matrix must be a matrix (list of lists) of integers/floats'
    sizerror = 'Each row of the matrix must have the same size'
    diverror = 'div must be a number'
    zererror = 'division by zero'

    """ que matrix sea lista """
    if not isinstance(matrix, list):
        raise TypeError(typerror)

    """ elementos de la matrix deben ser listas """
    if not all([isinstance(row, list) for row in matrix]):
        raise TypeError(typerror)

    """ las listas deben tener el mismo tamaño """
    if len(set([len(row) for row in matrix])) != 1:
        raise TypeError(sizerror)

    """ los elementos dentro de cada row en matrix deben ser int or float """
    for item in [item for row in matrix for item in row]:
        if not isinstance(item, (int, float)):
            raise TypeError(typerror)

    """ div debe ser integer or float """
    if not isinstance(div, (int, float)):
        raise TypeError(diverror)

    """ div no debe ser cero """
    if div == 0:
        raise ZeroDivisionError(zererror)

    return ([[round(item / div, 2) for item in row] for row in matrix])
