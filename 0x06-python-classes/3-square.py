#!/usr/bin/python3
# 3-square.py
"""Define a class Square."""


class Square:
    """square class."""

    def __init__(self, asz=0):
        """Init a new square.

        Args:
            asz (int): The size of the new square.
        """
        if not isinstance(asz, int):
            raise TypeError("asz must be an integer")
        elif asz < 0:
            raise ValueError("asz must be >= 0")
        self.__size = asz

    def area(self):
        """Return the area of the square."""
        return (self.__size * self.__size)

