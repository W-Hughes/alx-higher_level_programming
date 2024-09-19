#!/usr/bin/python3

def weight_average(my_list=[]):
    if not my_list:
        return (0)

    sum_ = 0
    freq = 0

    for tup in my_list:
        sum_ += tup[0] * tup[1]
        freq += tup[1]

    weighted_mean = sum_ / freq

    return (weighted_mean)
