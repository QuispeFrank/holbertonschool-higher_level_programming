#!/usr/bin/python3
""" Roman to Integer """


def roman_to_int(roman_string):
    """ converts a Roman numeral to an integer """
    if not isinstance(roman_string, str):
        return 0

    r_dic = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    num = 0
    romans = list(roman_string)

    for i in range(len(romans)):
        if (i != len(romans) - 1) and r_dic[romans[i]] >= r_dic[romans[i + 1]]:
            num = num + r_dic[romans[i]]
        elif i == len(romans) - 1:
            num = num + r_dic[romans[i]]
        else:
            num = num - r_dic[romans[i]]
    return num
