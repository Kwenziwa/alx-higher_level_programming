#!/usr/bin/python3
# 10-divisible_by_2.py

def divisible_by_2(mylist=[]):
    multi = []
    for i in range(len(mylist)):
        if mylist[i] % 2 == 0:
            multi.append(True)
        else:
            multi.append(False)

    return (multi)
