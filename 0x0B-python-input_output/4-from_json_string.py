#!/usr/bin/python3
# 4-from_json_string.py
"""
==================================
Defines a JSON-to-object function.
==================================
"""
import json


def from_json_string(a_string):
    """Python object representation of a JSON string returned."""
    return json.loads(a_string)
