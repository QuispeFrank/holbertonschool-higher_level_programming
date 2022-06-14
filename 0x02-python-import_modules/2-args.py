#!/usr/bin/python3
""" How to make a script dynamic! """


if __name__ == "__main__":
    from sys import argv

    if len(argv) == 1:
        print(f'0 arguments.')
    elif len(argv) == 2:
        print(f'1 argument:')
    else:
        print(f'{len(argv) - 1} arguments:')

    for index in range(1, len(argv)):
        print(f'{index}: {argv[index]}')
