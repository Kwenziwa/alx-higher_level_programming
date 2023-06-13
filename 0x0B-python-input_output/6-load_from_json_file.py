#!/usr/bin/python3
# 6-load_from_json_file.py
"""
=====================================
Defines a JSON file-reading function.
=====================================
"""
import json


def load_from_json_file(filename):
    """Python object from a JSON file created."""
    with open(filename) as z:
        return json.load(z)
