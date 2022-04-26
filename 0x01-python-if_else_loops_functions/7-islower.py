#!/usr/bin/python3
def islower(c):
    for i in range(97, 123):
        if c == ord(i):
            return True
    return False
