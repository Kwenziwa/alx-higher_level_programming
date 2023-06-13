#!/usr/bin/python3
# 3-to_json_string.py
"""
===============================
string-to-JSON function defined.
===============================
"""
import json


def to_json_string(my_obj):
    """JSON representation of a string object returned."""
    return json.dumps(my_obj)

