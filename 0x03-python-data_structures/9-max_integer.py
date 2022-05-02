#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list != []:
        max_value = my_list[0]
        for number in my_list:
            if number >= max_value:
                max_value = number
        return(max_value)
    return None
