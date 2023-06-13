#!/usr/bin/python3
# 3-write_file.py
"""
=====================================
File-writting function defined.
=====================================
"""

def write_file(filename="", text=""):
    with open(filename, "w", encoding="utf-8") as a_content:
        return a_content.write(text)
