#!/usr/bin/python3
def weight_average(my_list):
    total = 0
    weight_tot = 0
    if len(my_list) == 0:
        return total
    for i in my_list:
        total += i[0] * i[1]
        weight_tot += i[1]
    return total / weight_tot
