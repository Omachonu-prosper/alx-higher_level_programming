#!/usr/bin/env python3

def no_c(my_string):
    new_string = my_string[:]

    for i in range(0, len(my_string)):
        if new_string[i] in ['c', 'C']:
            new_string = new_string[:i] + '' + new_string[i+1:]

    return new_string
