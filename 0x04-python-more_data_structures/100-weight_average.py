#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is None or my_list == []:
        return 0
    total_weight, total_score = 0, 0
    for x, y in my_list:
        total_score += y
        multiplication = x * y
        total_weight += multiplication
    return total_weight/total_score
