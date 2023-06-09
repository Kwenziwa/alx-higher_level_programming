#!/usr/bin/python3
# 100-safe_print_integer_err.py
import sys

def safe_print_integer_err(a_value):
    try:
        print("{:d}".format(a_value))
        return (True)
    except (TypeError, ValueError):
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (False)
