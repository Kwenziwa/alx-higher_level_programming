#!/usr/bin/python3
# 2-square.py
"""Declare a class Square."""


class Square:
    """square Represent."""

    def __init__(self, dimension=0):
        """Square new Initializer .

        Args:
            dimension (int): The dimension of the new square.
        """
        if not isinstance(dimension, int):
            raise TypeError("The dimension must be a whole number.")
        elif dimension < 0:
            raise ValueError("dimension must be greater or equal 0")
        self.__size = dimension
