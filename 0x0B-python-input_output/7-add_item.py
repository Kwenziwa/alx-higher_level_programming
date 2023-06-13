#!/usr/bin/python3
# 7-add_item.py
""" 
========================================================
Python list with all argumentst and save them to a file.
========================================================
"""
import sys

if __name__ == "__main__":
    save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('8-load_from_json_file').load_from_json_file

    try:
        all_items = load_from_json_file("add_item.json")
    except FileNotFoundError:
        all_items = []
    all_items.extend(sys.argv[1:])
    save_to_json_file(all_items, "add_item.json")
