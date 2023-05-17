#!/usr/bin/python3
# 0-square_matrix_simple.py
def square_matrix_simple(mtx=[]):
    sqd = []
    for line in mtx:
        sqd.append([c**2 for c in line])
    return sqd
