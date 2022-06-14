#!/usr/bin/python3
""" Import a simple function from a simple file """


if __name__ == "__main__":
    import add_0 as module
    print(f'1 + 2 = {module.add(1, 2)}')
