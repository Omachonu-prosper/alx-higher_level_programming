#!/usr/bin/python3

"""Exports the append_write function."""


def append_write(filename="", text=""):
    """Appends a string at the end of a file
    returns the number of characters added."""
    with open(filename, 'a') as f:
        return f.write(text)
