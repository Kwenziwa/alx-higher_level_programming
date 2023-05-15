#!/usr/bin/python3
# 3-print_reversed_list_integer.py
def print_reversed_list_integer(all_list=[]):
    if all_list is None:
        return
    for x in reversed(all_list):
        print('{:d}'.format(x))

