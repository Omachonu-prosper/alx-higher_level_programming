#!/usr/bin/python3

import sys


def infinite_add():
    result_of_addition = 0

    for i in range(1, len(sys.argv)):
        result_of_addition += int(sys.argv[i])

    print(result_of_addition)


if __name__ == "__main__":
    infinite_add()
