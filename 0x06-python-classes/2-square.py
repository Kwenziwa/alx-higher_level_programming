#!/usr/bin/python3
# 2-square.py
""" Declare a class Square."""


class Square:
    """ square Represent."""

    def __init__(self, size=0):
        """Square new Initializer .

        Args:
            size (int): The dimension of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("The dimension must be a whole number.")
        elif size < 0:
            raise ValueError("dimension must be greater or equal 0")
        self.__size = size
