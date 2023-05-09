#!/usr/bin/python3
# 6-print_comb3.py

for anum1 in range(0, 10):
    for anum2 in range(anum1 + 1, 10):
        if anum1 == 8 and anum2 == 9:
            print("{}{}".format(anum1, anum2))
        else:
            print("{}{}".format(anum1, anum2), end=", ")
