#!/usr/bin/python3

"""Creates a rectangle class with height and width attributes.

Example usage:
    import 3-rectangle as rectangle
    rectangle3 = rectangle.Rectangle()
"""


class Rectangle:
    """Rectangle class which defines properties for a rectangle."""
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Constructor function for this class."""
        self.checkWidth(width)
        self.checkHeight(height)
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ''
        else:
            return '\n'.join(
                str(self.print_symbol)
                *
                self.__width for i in range(self.__height)
                )

    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print('Bye rectangle...')
        return

    @property
    def width(self):
        """Getter for the width attribute."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for the width attribute"""
        self.checkWidth(value)
        self.__width = value

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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')

        return rect_2 if rect_2.area() > rect_1.area() else rect_1