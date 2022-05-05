#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    b_dictionary = a_dictionary.copy()
    for key in b_dictionary:
        if b_dictionary[key] == value:
            del a_dictionary[key]
    return a_dictionary
