#!/usr/bin/python3
""" Pascal's Triangle """


def pascal_triangle(num):
    """ returns a list of lists of integers representing
        the Pascal’s triangle of n.
    """
    if num <= 0:
        return []

    p = [[1]]
    for r in range(1, num):
        p.append([1] + [p[r-1][n-1] + p[r-1][n] for n in range(1, r)] + [1])
    return p
