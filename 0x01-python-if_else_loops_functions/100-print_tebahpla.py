#!/usr/bin/python3
""" Smile in the mirror """


for c in range(ord('z'), ord('a') - 1, -1):
    print(f'{chr(c) if c % 2 == 0 else chr(c - 32)}', end='')
