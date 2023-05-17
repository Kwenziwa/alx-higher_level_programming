#!/usr/bin/python3
# 6-print_sorted_dictionary.py
def print_sorted_dictionary(dict):
    for i in sorted(dict.keys()):
        print("{}: {}".format(i, dict[i]))
