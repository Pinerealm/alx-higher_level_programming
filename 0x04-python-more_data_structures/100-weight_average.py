#!/usr/bin/python3
def weight_average(my_list):
    total = 0
    for i in my_list:
        total += i[0] * i[1]
    return total / sum(i[1] for i in my_list)
