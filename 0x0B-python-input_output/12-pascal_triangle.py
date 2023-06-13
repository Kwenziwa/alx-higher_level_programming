#!/usr/bin/python3
# 12-pascal_triangle.py
"""
====================================
Defines a Pascal's Triangle function.
====================================
"""


def pascal_triangle(v):
    """Pascal's Triangle of size v Represent .

    Returns a list of lists of integers representing the triangle.
    """
    if v<= 0:
        return []

    triangles = [[1]]
    while len(triangles) != v:
        tri = triangles[-1]
        tempo = [1]
        for i in range(len(tri) - 1):
            tempo.append(tri[i] + tri[i + 1])
        tempo.append(1)
        triangles.append(tempo)
    return triangles
