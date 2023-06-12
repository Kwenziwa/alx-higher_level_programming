#!/usr/bin/python3
# 9-rectangle.py
"""
===================================
Rectangle that inherits from BaseGeometry.
===================================
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """Presenter a rectangle using BaseGeometry."""

    def __init__(self, width, height):
        
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """send the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """send the print() and str() representation of a Rectangle."""
        out_string = "[" + str(self.__class__.__name__) + "] "
        out_string += str(self.__width) + "/" + str(self.__height)
        return out_string
