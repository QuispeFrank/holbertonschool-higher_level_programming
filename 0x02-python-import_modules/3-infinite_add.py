#!/usr/bin/python3
""" Infinite addition """


if __name__ == "__main__":
    from sys import argv
    print(sum([int(argv[n]) for n in range(1, len(argv))]))
