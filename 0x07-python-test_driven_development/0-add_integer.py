#!/usr/bin/python3
# 0-add_integer.py

def add_integer(x, y=98):
    if ((not isinstance(x, int) and not isinstance(x, float))):
        raise TypeError("x must be an integer")
    if ((not isinstance(y, int) and not isinstance(y, float))):
        raise TypeError("y must be an integer")
    return (int(x) + int(y))
