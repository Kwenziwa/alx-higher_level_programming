#!/usr/bin/python3
# 5-save_to_json_file.py
"""
=====================================
Defines a JSON file-writing function.
=====================================
"""
import json


def save_to_json_file(my_obj, filename):
    """Writting a object into a text file using JSON representation."""
    with open(filename, "w") as z:
        json.dump(my_obj, z)
