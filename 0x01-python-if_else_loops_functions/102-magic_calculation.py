#!/usr/bin/python3
""" ByteCode -> Python #2 """


def magic_calculation(a, b, c):
    if a < b:
        return c
    if c > b:
        return a + b
    return a * b - c
