#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):

    items = 0
    for idx in range(x):
        try:
            print("{:d}".format(my_list[idx]), end="")
            items += 1
        except TypeError:
            continue
        except ValueError:
            continue
    print("")

    return items
