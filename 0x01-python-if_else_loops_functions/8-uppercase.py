#!/usr/bin/python3
def uppercase(str):
    if str == "":
        print("")
        return
    for i in range(len(str)):
        a = ""
        if (i == len(str) - 1):
            a = "\n"
        if ord(str[i]) >= 97 and ord(str[i]) <= 122:
            print(f"{chr(ord(str[i]) - 32)}", end=a)
        else:
            print("{}".format(str[i]), end=a)
