#!/usr/bin/python3

"""Creates a rectangle class with height and width attributes.

Example usage:
    import 3-rectangle as rectangle
    rectangle3 = rectangle.Rectangle()
"""


class Rectangle:
    """Rectangle class which defines properties for a rectangle."""

    def __init__(self, width=0, height=0):
        """Constructor function for this class."""
        self.checkWidth(width)
        self.checkHeight(height)

        self.__width = width
        self.__height = height

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ''
        else:
            return '\n'.join('#' * self.__width for i in range(self.__height))

    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)

    @property
    def width(self):
        """Getter for the width attribute."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for the width attribute"""
        self.checkWidth(value)
        self.__width = value
        return

    @property
    def height(self):
        """Getter for the height attribute."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for the height attribute."""
        self.checkHeight(value)
        self.__height = value
        return

    def checkWidth(self, width):
        if type(width) is not int:
            raise TypeError('width must be an integer')
        if width < 0:
            raise ValueError('width must be >= 0')

    def checkHeight(self, height):
        if type(height) is not int:
            raise TypeError('height must be an integer')
        if height < 0:
            raise ValueError('height must be >= 0')

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the perimeter of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__height * 2) + (self.__width * 2)
