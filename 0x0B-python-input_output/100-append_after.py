#!/usr/bin/python3
# 100-append_after.py
"""
======================================
Defines a text file insertion function.
======================================
"""


def append_after(filename="", search_string="", new_string=""):
    """Inserting text after each line containing a given string in a file.

    Args:
        filename (str): name of the file.
        search_string (str): string to search for within the file.
        new_string (str): string to insert.
    """
    tempo_text = ""
    with open(filename) as r:
        for line in r:
            tempo_text += line
            if search_string in line:
                tempo_text += new_string
    with open(filename, "w") as w:
        w.write(tempo_text)
