#!/usr/bin/python3
# 1-my_list.py

"""Class MyList defines an inherited list ."""

class MyList(list):

    """printing for the built-in list class Implemented."""

    def print_sorted(self):
        """Printing a list in sorted in a ascending order."""
        print(sorted(self))
