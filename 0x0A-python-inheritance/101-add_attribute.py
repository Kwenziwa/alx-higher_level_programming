#!/usr/bin/python3
# 101-add_attribute.py
"""The function that adds attributes to objects."""


def add_attribute(obj, att, value):
  
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
