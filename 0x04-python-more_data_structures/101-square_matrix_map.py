#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return(list(list(map(lambda item: item ** 2, row)) for row in matrix))
