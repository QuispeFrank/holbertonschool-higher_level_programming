#!/usr/bin/python3
for dec in range(0, 8):
    for uni in range(0, 10):
        if uni > dec:
            print("{}{}, ".format(dec, uni), end="")
print(89)
