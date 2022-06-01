#!/usr/bin/python3
"""Function that returns a list of lists
of integers representing the Pascal’s triangle of"""


def pascal_triangle(n):
    """Returns a list of integers
        n : number of triangle size
    """

    if n <= 0:
        return []
    if n == 1:
        return [[1]]
    if n == 2:
        return [[1], [1, 1]]

    tr_p = [[1], [1, 1]]

    for i in range(2, n):
        lista = [1]
        for j in range(1, i):
            lista.append(tr_p[i-1][j-1] + tr_p[i-1][j])
        lista.append(1)
        tr_p.append(lista)
    return(tr_p)
