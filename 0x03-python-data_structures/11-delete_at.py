#!/usr/bin/python3
# 11-delete_at.py
def delete_at(mylist=[], ids=0):
    if 0 <= ids < len(mylist):
        del(mylist[ids])
    return(mylist)
