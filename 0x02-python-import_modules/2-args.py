#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    # tamaño del argv
    args = len(sys.argv) - 1
    if args == 0:
        print(f"{args} arguments.")
    elif args == 1:
        print(f"{args} argument:")
    else:
        print(f"{args} arguments:")

    for i in range(1, args + 1):
        print(f"{i}: {sys.argv[i]}")
