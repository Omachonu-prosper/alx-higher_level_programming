#!/usr/bin/python3

def uppercase(str):
    for i in str:
        ascii_of_i = ord(i)

        if ascii_of_i in range(97, 123):
            i = ascii_of_i - 32
        else:
            i = ascii_of_i

        print("{i:c}".format(i=i), end="")

    print()
