#!/usr/bin/python3
""" Import a simple function from a simple file """


if __name__ == "__main__":
    import add_0 as module
    a = 1
    b = 2
    print(f'{a} + {b} = {module.add(a, b)}')
