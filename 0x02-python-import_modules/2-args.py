#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args = len(sys.argv) - 1
    print(f"{args} arguments.")
    for i in range(1, args + 1):
        print(f"{i}: {sys.argv[i]}")
