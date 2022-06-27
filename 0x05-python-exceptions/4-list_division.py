#!/usr/bin/python3
""" Divide a list """


def list_division(my_list_1, my_list_2, list_length):
    """ function that divides element by element 2 lists.

    Args:
        my_list_1: first list.
        my_list_2: second list.
        list_length: number of divisions.
    """

    div_list = []
    res = None
    for idx in range(list_length):
        try:
            res = my_list_1[idx] / my_list_2[idx]

        except ZeroDivisionError:
            print("division by 0")
            res = 0
        except TypeError:
            print("wrong type")
            res = 0
        except IndexError:
            print("out of range")
            res = 0
        finally:
            div_list.append(res)

    return div_list
