#!/usr/bin/python3
""" Who are you? """


if __name__ == "__main__":
    import hidden_4

    attributes = dir(hidden_4)
    for attr in attributes:
        print(end=attr + '\n' if attr[:2] != '__' else '')
