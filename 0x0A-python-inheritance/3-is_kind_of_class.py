#!/usr/bin/python3
# 3-is_kind_of_class.py
"""
===================================
 A defined class and inherited class-checking function.
===================================
"""
def is_kind_of_class(obj, a_class):
    """Method that return True if an object is an instance of a class
    that inherited from"""

    return isinstance(obj, a_class)
