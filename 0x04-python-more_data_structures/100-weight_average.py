#!/usr/bin/python3
def weight_average(my_list=[]):
    suma, div = (0, 0)
    for score in my_list:
        suma += score[0] * score[1]
        div += score[1]
    return suma / div
