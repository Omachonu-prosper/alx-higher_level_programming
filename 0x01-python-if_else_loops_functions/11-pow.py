#!/usr/bin/python3

def pow(a, b):
    current_value = a

    if b == 0:
        return 1

    for i in range(0, b - 1):
        current_value *= a
        
    return current_value
