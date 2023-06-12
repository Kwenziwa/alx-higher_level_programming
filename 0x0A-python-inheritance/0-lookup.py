#!/usr/bin/python3
# 0-lookup.py
"""As we define an lookup function attribute object."""
def lookup(a_object):
    """Return a object list of available attributes."""
    return (dir(a_object))
