#!/usr/bin/python3

"""Creates a new square class.

This new class has more features than the previous classes.

Typical usage example:
    import 3-square
"""


class Square:
    """
    class square that has attributes:
        size
    some attributes are protected from input.
    """
    def __init__(self, size=0):
        """
        initialization function for our square clasee
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        calculates the area of the square
        """
        return self.__size ** 2
