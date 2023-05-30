#!/usr/bin/python3
# 6-square.py
# Brennan D Baraban <375@holbertonschool.com>
"""Declare a class Square."""


class Square:
    """Square Represent"""

    def __init__(self, size=0, position=(0, 0)):
        """New square Initializer.

        Args:
            size (int): The size of the square.
            position (int, int): The position of the a square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Setter/Getter the presemt square size."""
        return (self.__size)

    @size.setter
    def size(self, nx):
        if not isinstance(nx, int):
            raise TypeError("size required to be integer")
        elif nx < 0:
            raise ValueError("size required to be >= 0")
        self.__size = nx

    @property
    def position(self):
        """Getter/Setter the present position of the square."""
        return (self.__position)

    @position.setter
    def position(self, nx):
        if (not isinstance(nx, tuple) or
                len(nx) != 2 or
                not all(isinstance(num, int) for num in nx) or
                not all(num >= 0 for num in nx)):
            raise TypeError("must be a tuple of 2 positive int")
        self.__position = nx

    def area(self):
        """Return the present area of the square."""
        return (self.__size * self.__size)

    def my_print(self):
        """Print a square with the # character."""
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
