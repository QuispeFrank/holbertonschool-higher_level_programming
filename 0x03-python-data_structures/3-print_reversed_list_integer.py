#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list is None:
        print()
        return None
    new_list = my_list.copy()
    new_list.reverse()
    for item in new_list:
        print(item)
