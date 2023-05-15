#!/usr/bin/python3
# 1-element_at.py
def element_at(alist, ids):
    return(alist[ids] if 0 <= ids < len(alist) else "None")
