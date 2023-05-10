#!/usr/bin/python3
# 101-remove_char_at.py


def remove_char_at(astring, n):
    if n < 0:
        return (astring)
    return (astring[:n] + astring[n+1:])
