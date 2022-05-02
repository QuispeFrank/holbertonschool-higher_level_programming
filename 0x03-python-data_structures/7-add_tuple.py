#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) == 0:
        t_a = (0, 0)
    elif len(tuple_a) == 1:
        t_a = (tuple_a[0], 0)
    else:
        t_a = tuple_a

    if len(tuple_b) == 0:
        t_b = (0, 0)
    elif len(tuple_b) == 1:
        t_b = (tuple_b[0], 0)
    else:
        t_b = tuple_b

    return (t_a[0] + t_b[0], t_a[1] + t_b[1])
