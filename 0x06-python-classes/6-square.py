#!/usr/bin/python3
# 6-square.py
"""Declare a class Square."""


class Square:
    """Square Represent"""

    def __init__(self, size=0, posi=(0, 0)):
        """New square Initializer.

        Args:
            size (int): The size of the square.
            posi (int, int): The position of the a square.
        """
        self.size = size
        self.posi = posi

    @property
    def size(self):
        """Set/Get the presemt square size."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def posi(self):
        """Get/set the current posi of the square."""
        return (self.__position)

    @posi.setter
    def posi(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("posi must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the current area of the square."""
        return (self.__size * self.__size)

    def my_print(self):
        """Print the square with the # character."""
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
