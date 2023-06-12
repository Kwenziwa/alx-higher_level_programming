#!/usr/bin/python3
# 7-base_geometry.py
"""
===================================
Defines a base geometry class BaseGeometry.
===================================
"""

class BaseGeometry:
    """Class BaseGeometry """

    def area(self):
        """function for calculated area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Function for validate if a num is integer"""

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
