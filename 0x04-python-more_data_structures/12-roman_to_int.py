#!/usr/bin/python3
def roman_to_int(roman_string):
    total = 0
    prev_value = 0
    prev_total = 0
    if roman_string is None or type(roman_string) is not str:
        return 0
    else:
        for char in reversed(roman_string):
            if char == 'I':
                total += 1
            elif char == 'V':
                total += 5
            elif char == 'X':
                total += 10
            elif char == 'L':
                total += 50
            elif char == 'C':
                total += 100
            elif char == 'D':
                total += 500
            elif char == 'M':
                total += 1000
            if prev_value > total - prev_total:
                total = total - (2 * (total - prev_total))
            prev_total = total
            prev_value = total - prev_total
    return total
