#!/usr/bin/python3

"""Exports the write_file function."""


def write_file(filename="", text=""):
    """function that writes to a file and returns the number of chars writtten."""
    with open(filename, 'w') as f:
        return f.write(text)