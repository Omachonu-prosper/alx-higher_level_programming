#!/usr/bin/python3

"""The function that prints My name is <first name> <last name>

First name and last name must be strings
"""


def say_my_name(first_name, last_name=""):
    """Prints out given name in specific format.

    First name and last name must be strings

    Example input:
    >>> say_my_name("John", "Smith")

    Example output:
    My name is John Smith
    """
    if type(first_name) is not str:
        raise TypeError('first_name must be a string')
    if type(last_name) is not str:
        raise TypeError('last_name must be a string')
    if last_name:
        last_name = ' ' + last_name

    print("My name is {}{}".format(first_name, last_name))
