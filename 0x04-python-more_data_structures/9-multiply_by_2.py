#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    dic_copy = a_dictionary.copy()
    for item in dic_copy:
        dic_copy[item] *= 2
    return dic_copy
