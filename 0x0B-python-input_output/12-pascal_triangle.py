#!/usr/bin/python3
"""Function that returns a list of lists
of integers representing the Pascal’s triangle of"""


def pascal_triangle(num):
    """Returns a list of integers
        n : number of triangle size
    """
    p = [[1]]
    for r in range(1, num):
        p.append([1] + [p[r-1][n-1] + p[r-1][n] for n in range(1, r)] + [1])
    return p
