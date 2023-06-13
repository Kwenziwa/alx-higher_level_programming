#!/usr/bin/python3
# 0-read_file.py

"""
=====================================
File-reading function defined.
=====================================
"""

def read_file(filename=""):
    """Printing a contents of a UTF8 text file to stdout."""
    with open(filename, encoding="utf-8") as a_content:
        print(a_content.read(), end="")
