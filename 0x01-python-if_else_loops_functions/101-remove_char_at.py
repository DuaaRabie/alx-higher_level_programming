#!/usr/bin/python3
def remove_char_at(str, n):
    str_cpy = ""
    for index in range(len(str)):
        if index != n:
            str_cpy += str[index]
    return str_cpy
