#!/usr/bin/python3
# 8-uppercase.py


def uppercase(astring):
    for c in astring:
        if ord(c) >= 97 and ord(c) <= 122:
            c = chr(ord(c) - 32)
        print("{}".format(c), end="")
    print("")
