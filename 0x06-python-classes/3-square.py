#!/usr/bin/python3
# 3-square.py
class Square:
    """ Declare Square class"""
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size should be integer")
        elif size < 0:
            raise ValueError("size should be >= 0")
        else:
            self.__size = size

    def area(self):
        return self.__size * self.__size
