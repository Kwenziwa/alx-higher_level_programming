#!/usr/bin/python3
# 1-rectangle.py
class Rectangle:
    
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width should be integer")
        if value < 0:
            raise ValueError("width should be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height should be integer")
        if value < 0:
            raise ValueError("height should be >= 0")
        self.__height = value
