#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if len(matrix) == 1 and len(matrix[0]) == 0:
        print()
        return

    for i in matrix:
        for j in range(0, len(i)):
            if j == len(i) - 1:
                print("{}".format(i[j]))
            else:
                print("{}".format(i[j]), end=" ")
