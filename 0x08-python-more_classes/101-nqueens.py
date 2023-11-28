#!/usr/bin/python3
""" This model for N queen """


import sys

if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)
elif not sys.argv[1].isdigit():
    print("N must be a number")
    sys.exit(1)
elif int(sys.argv[1]) < 4:
    print("N must be at least 4")
    sys.exit(1)
for i in range(int(sys.argv[1])):
    pass
