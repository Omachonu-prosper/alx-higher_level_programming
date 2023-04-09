#!/usr/bin/python3

"""This module provides a function to divide a matrix.

A number is passed as the second arguement to the function.
This number is used to divide all elements in the matrix
"""


def matrix_divided(matrix, div):
    """Divides a matrix by div.

    Matrix must be a list of integers/floats
    Div must be an integer or float greater than 0
    Each row of the matrix must be the same size
    All elements in the matrix are divided by div and
    rounded to 2 decimal places
    Returns a new matrix

    Example Input:
    matrix = [
        [1, 2, 3],
        [4, 5, 6]
    ]
    print(matrix_divided(matrix, 3))
    print(matrix)

    Example Output:
    [[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]
    [[1, 2, 3], [4, 5, 6]]
    """
    if type(matrix) is not list or len(matrix) is 0:
        raise TypeError(
            'matrix must be a matrix (list of lists) of integers/floats'
            )

    if div is None or not (type(div) is int or type(div) is float):
        raise TypeError('div must be a number')

    if div == 0:
        raise ZeroDivisionError('division by zero')

    new_matrix = []
    row_length = len(matrix[0])

    for row in matrix:
        if len(row) != row_length:
            raise TypeError('Each row of the matrix must have the same size')

        new_row = []
        for i in row:
            if i is None or not (type(i) is int or type(i) is float):
                raise TypeError(
                    'matrix must be a matrix \
                    (list of lists) of integers/floats'
                    )

            new_row.append(round(i / div, 2))
        new_matrix.append(new_row)

    return new_matrix
