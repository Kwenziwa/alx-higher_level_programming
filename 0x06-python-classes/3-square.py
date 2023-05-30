#!/usr/bin/python3
# 3-square.py
class Square:
    """ Declare Square class"""
    def __init__(self, dms=0):
        if type(dms) != int:
            raise TypeError("size must be an integer")
        elif dms < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = dms

    def area(self):
        return self.__size * self.__size
