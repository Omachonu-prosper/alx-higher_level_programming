#!/usr/bin/python3

"""Creates a rectangle class with height and width attributes.

Example usage:
    import 1-rectangle as rectangle
    rectangle1 = rectangle.Rectangle()
"""


class Rectangle:
    """Rectangle class which defines properties for a rectangle."""

    def __init__(self, width=0, height=0):
        """Constructor function for this class.

        Instantiates private attributes width and height to 0"""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Getter for the width attribute."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for the width attribute"""
        if type(value) != int:
            raise TypeError('Width must be an integer')

        if value < 0:
            raise ValueError('Width must be >= 0')

        self.__width = value
        return

    @property
    def height(self):
        """Getter for the height property."""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError('Height must be an integer')

        if value < 0:
            raise ValueError('Height must be >= 0')

        self.__height = value
        return
