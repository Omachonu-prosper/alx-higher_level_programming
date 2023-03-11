#!/usr/bin/python3

import hidden_4


def print_names():
    names = dir(hidden_4)
    
    for i in names:
        if "__" not in i:
            print("{}".format(i))


if __name__ == "__main__":
    print_names()
