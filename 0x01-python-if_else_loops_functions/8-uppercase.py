#!/usr/bin/python3
def uppercase(str):
    for i in str:
        asci = chr(ord(i) - 32)
        print(f"{asci if ord(i) >= 97 and ord(i) <= 122 else i}", end="")
    print("")
