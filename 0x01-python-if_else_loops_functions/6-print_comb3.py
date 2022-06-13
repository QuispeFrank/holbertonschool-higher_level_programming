#!/usr/bin/python3
""" Inventing is a combination of brains and materials.
    The more brains you use, the less material you need
"""


for dec in range(0, 9):
    for uni in range(dec + 1, 10):
        print(f'{dec}{uni}', end=', ' if dec != 8 else '\n')
