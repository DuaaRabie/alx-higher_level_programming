#!/usr/bin/python3
import random
number = random.randint(-10, 10)
print(number, end=" ")
if number > 0:
    print("is positive")
elif number == 0:
    print("is 0")
elif number < 0:
    print("is negative")
