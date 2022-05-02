#!/usr/bin/python3
def no_c(my_string):
    if isinstance(my_string, str) is True:
        new_string = ""
        for letter in my_string:
            if letter != 'c' and letter != 'C':
                new_string = new_string + letter
        return(new_string)
