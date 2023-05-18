#!/usr/bin/python3
# 102-complex_delete.py
def complex_delete(a_dict, value):
    tempo = a_dict.copy()
    for k, v in tempo.items():
        if value == v:
            a_dict.pop(k)
    return a_dict
