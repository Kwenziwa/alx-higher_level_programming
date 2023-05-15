#!/usr/bin/python3
# 6-print_matrix_integer.py
def print_matrix_integer(the_matrix=[[]]):
    for x in the_matrix:
        print(' '.join('{:d}'.format(j)for j in x))
