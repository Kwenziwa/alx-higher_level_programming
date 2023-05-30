#!/usr/bin/python3
# 4-square.py
"""Declare a class Square."""


class Square:
    """Represent a square."""

    def __init__(self, asz=0):
        """Init a new square.

        Args:
            asz (int): The size of the  square.
        """
        self.asz = asz

    @property
    def asz(self):
        """G/s  the size of the square."""
        return (self.__size)

    @asz.setter
    def asz(self, value):
        if not isinstance(value, int):
            raise TypeError("size be required to be an integer")
        elif value < 0:
            raise ValueError("size be required to be >= 0")
        self.__size = value

    def area(self):
        """Return the area of the square."""
        return (self.__size * self.__size)
