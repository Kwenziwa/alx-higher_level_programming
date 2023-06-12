#!/usr/bin/python3
# 7-base_geometry.py
"""
===================================
Defines a base geometry class BaseGeometry.
===================================
"""


class BaseGeometry:
   
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        All Action
        """
        if type(value) != int:
            raise TypeError("{} shuould be an integer".format(name))
        if value <= 0:
            raise ValueError("{} should be greater than 0".format(name))
