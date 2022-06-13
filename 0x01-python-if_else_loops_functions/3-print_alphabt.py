#!/usr/bin/python3
""" When I was having that alphabet soup,
    I never thought that it would pay off.
"""


for letter in range(ord('a'), ord('z') + 1):
    if(chr(letter) != 'e' and chr(letter) != 'q'):
        print(chr(letter), end='')
