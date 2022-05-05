#!/usr/bin/python3
def roman_to_int(roman_string):
    if isinstance(roman_string, str) is False:
        return 0

    r_dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    if len(roman_string) == 0:
        return None
    romans = list(roman_string)
    num = 0
    for i in range(len(romans)):
        if (i != len(romans) - 1) and r_dic[romans[i]] >= r_dic[romans[i + 1]]:
            num = num + r_dic[romans[i]]
        elif i == len(romans) - 1:
            num = num + r_dic[romans[i]]
        else:
            num = num - r_dic[romans[i]]
    return num
