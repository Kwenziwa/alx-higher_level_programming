#!/usr/bin/python3
# 11-student.py
"""
=======================
A class Student Defines.
=======================
"""



class Student:
    """ a student represent."""

    def __init__(self, first_name, last_name, age):
        """Ini a new Student.

        Args:
            first_name (str): firstname of the student.
            last_name (str): lastname of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Dictionary representation of the Student."""
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """The Student Replace all attributes.

        Args:
            json (dict): The key/value pairs to replace attributes with.
        """
        for k, v in json.items():
            setattr(self, k, v)

