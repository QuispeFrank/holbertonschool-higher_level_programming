#!/usr/bin/python3
""" Only by 2 """


def divisible_by_2(my_list=[]):
    """ finds all multiples of 2 in a list """
    return(list(map(lambda n: not n % 2, my_list)))
