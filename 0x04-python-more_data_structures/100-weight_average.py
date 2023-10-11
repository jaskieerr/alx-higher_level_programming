#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list and len(my_list):
        sum = 0
        weight = 0
        for tup in my_list:
            sum += (tup[0] * tup[1])
            weight += tup[1]
        return (sum / weight)
    return 0
