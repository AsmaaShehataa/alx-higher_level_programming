#!/usr/bin/python3
"""
Class rectangle that defines a rectangle
"""


class Rectangle:
    """empty class Rectangle that defines a rectangle"""

    def __init__(self, width=0, height=0):
        """
        Constructor for the class Rectangle. It initializes an object of type
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        width getter
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        width setter
        """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise TypeError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """
        height getter
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        width setter
        """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value
