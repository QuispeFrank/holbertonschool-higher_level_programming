#!/usr/bin/python3
def uniq_add(my_list=[]):
    sets = {item for item in my_list}
    suma = 0
    for item in sets:
        suma += item
    return suma
