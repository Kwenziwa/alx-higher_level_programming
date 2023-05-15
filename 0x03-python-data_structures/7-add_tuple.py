#!/usr/bin/python3
# 7-add_tuple.py
def add_tuple(tuple_1=(), tuple_2=()):
    tuple_1 += (0, 0)
    tuple_2 += (0, 0)
    return(tuple_1[0] + tuple_2[0], tuple_1[1] + tuple_2[1])
