#!/usr/bin/python3
# 2-write_file.py
"""
=====================================
File-reading function defined.
=====================================
"""
def append_write(filename="", text=""):
    """ This writes a string to a text file (UTF8)  """
    with open(filename, "a", encoding="utf-8") as z:
        return z.write(text)
