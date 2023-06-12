#!/usr/bin/python3
# 2-is_same_class.py
"""
==================================
Defines a class-checking function.
==================================
"""

def is_same_class(a_object, a_class):
 
    if type(a_object) == a_class:
        return True
    return False
