#!/usr/bin/python3

"""The function that prints prints a square with the character #.

A size is provided (the size of the square)
"""


def print_square(size):
    """Prints a square on the console using the # character.

    Definition:
    def print_square(size):
        ...

    size is the size of the square
    size must be an intefer otherwise a TypeError is raised
    size cannot be less than 0 otherwise a ValueError is raised
    """
    if type(size) is not int:
        raise TypeError('size must be an integer')
    if size < 0:
        raise TypeError('size must be >= 0')

    for i in range(size):
        print("#" * size)
