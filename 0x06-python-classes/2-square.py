#!/usr/bin/python3

"""Creates a new square class.

This new class has more features than the previous classes.
- It raises a TypeError if the size of the square is not an
  integer and a ValueError if the size of the integer is negative

Typical usage example:
    square = Square()
"""


class Square:
    """
    class square that has attributes:
        size
    some attributes are protected from input.
    """
    def __init__(self, size=0):
        """
        the initialization function for the square class
        checks for input errors for size
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
