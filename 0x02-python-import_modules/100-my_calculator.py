#!/usr/bin/python3


if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    if len(sys.argv) == 4:
        a = int(sys.argv[1])
        operator = sys.argv[2]
        b = int(sys.argv[3])

        if operator == '+':
            print(f"{a} + {b} = {add(a,b)}")
        elif operator == '-':
            print(f"{a} - {b} = {sub(a,b)}")
        elif operator == '*':
            print(f"{a} * {b} = {mul(a,b)}")
        elif operator == '/':
            print(f"{a} / {b} = {div(a,b)}")
        else:
            print(f"Unknown operator. Available operators: +, -, * and /")
            exit(1)
    else:
        print(f"Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
