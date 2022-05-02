#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if isinstance(my_list, list):
        copy_list = my_list.copy()
        if idx >= 0 and idx < len(my_list):
            copy_list[idx] = element
        return(copy_list)
