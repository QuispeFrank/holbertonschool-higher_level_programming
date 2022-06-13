#!/usr/bin/python3
""" 00...99 """


for number in range(0, 100):
    print(f'{number:02}', end=', ' if number < 99 else '\n')
