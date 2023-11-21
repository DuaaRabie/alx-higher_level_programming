#!/usr/bin/python3
def magic_calculation(a, b):
    result = 0
    for i in range(1, 3):
        try:
            if i > a:
                result += a ** b / i
            else:
                reslut = a + b
        except:
            raise Exception("Too far")
    return result
