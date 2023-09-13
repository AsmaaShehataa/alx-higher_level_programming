#!/usr/bin/python3

def weight_average(my_list=[]):
    if not my_list:
        return
    num = 0
    x = 0

    for tup in my_list:
        num += tup[0] * tup[1]
        x += tup[1]
    return (num/x)
