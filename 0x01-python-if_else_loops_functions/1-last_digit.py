#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
digit = abs(number) % 10
if number < 0:
    digit = -digit
a = f"Last digit of {number} is {digit} and is"

if digit == 0:
    print(f"Last digit of {number} is 0 and is 0")
else:
    if number > 0:
        if digit > 5:
            print(f"{a} greater than 5")
        else:
            print(f"{a} less than 6 and not 0")
    else:
        digit = -digit
        print(f"{a} less than 6 and not 0")
