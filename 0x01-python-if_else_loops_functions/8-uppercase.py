#!/usr/bin/python3
""" To uppercase """


def uppercase(str):
    for c in str:
        c = chr(ord(c) - 32) if ord(c) in range(97, 123) else c
        print(c, end='')
    print('')
