#!/usr/bin/python3
for num1 in range(9):
    for num2 in range(1, 10):
        if num1 != num2 and num1 < num2:
            if num1 != 8 or num2 != 9:
                print("{}{},".format(num1, num2), end=" ")
            else:
                print("{}{}".format(num1, num2))
