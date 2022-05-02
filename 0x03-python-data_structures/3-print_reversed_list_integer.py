#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if isinstance(my_list, list) is True:
        my_list.reverse()
        for item in my_list:
            print("{:d}".format(item))
