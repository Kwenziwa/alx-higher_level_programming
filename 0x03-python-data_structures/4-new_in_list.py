#!/usr/bin/python3
# 4-new_in_list.py
def new_in_list(mylist, idx, elemnts):
    tmp_list = mylist[:]
    if 0 <= idx < len(mylist):
        tmp_list[idx] = elemnts
        return(tmp_list)
    return(mylist)
