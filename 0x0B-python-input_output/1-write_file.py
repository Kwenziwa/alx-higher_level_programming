#!/usr/bin/python3
# 3-write_file.py
"""
=====================================
File-writting function defined.
=====================================
"""

def write_file(filename="", text=""):
    """ Writes a string to a text file (UTF8)  """
    with open(filename, "w", encoding='utf-8') as z:
        return z.write(text)
