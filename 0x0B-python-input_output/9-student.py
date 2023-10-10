#!/usr/bin/python3
"""Classes: Student"""


class Student:
    """Student Class"""

    def __init__(self, first_name, last_name, age):
        """Constructor Method"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Dir Description"""
        return self.__dict__.copy()
