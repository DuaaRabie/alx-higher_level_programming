#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    length = len(sys.argv) - 1
    print("{} ".format(length), end="")
    print("{}".format("argument" if length <= 1 else "arguments"), end="")
    if length > 0:
        print(":")
        for i in range(1, length + 1):
            print("{}: {}".format(i, sys.argv[i]))
    else:
        print(".")
