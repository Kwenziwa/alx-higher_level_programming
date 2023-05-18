#!/usr/bin/python3
# 100-weight_average.py
def weight_average(alists=[]):
    if not alists:
        return 0

    num_avg = 0
    den_size = 0

    for tup in alists:
        num_avg += tup[0] * tup[1]
        den_size += tup[1]

    return (num_avg / den_size)
