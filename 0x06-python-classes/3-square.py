#!/usr/bin/python3
# 3-square.py
"""Define a class Square."""

class Square:

    def __init__(self, size=0):
       
        if not isinstance(size, int):
            raise TypeError("size should be an int")
        elif size < 0:
            raise ValueError("size is not >= 0")
        self.__size = size

    def area(self):
       
        return (self.__size * self.__size)
