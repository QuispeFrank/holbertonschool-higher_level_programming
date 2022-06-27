#!/usr/bin/python3
""" Safe list printing """


def safe_print_list(my_list=[], x=0):
    """ function that prints x elements of a list.

    Args:
        my_list: can contain any type (integer, string, etc.)
        x: the number of elements to print.
    """
    counter = 0
    for index in range(x):
        try:
            print(f'{my_list[index]}', end='')
            counter += 1
        except IndexError:
            break
    print('')

    return counter
