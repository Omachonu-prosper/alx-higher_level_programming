#!/usr/bin/python3
# Find peak module

def find_peak(list_of_integers):
    # finds a peak in a list of unsorted integers
    if len(list_of_integers) < 1:
        return None

    peak = list_of_integers[0]
    for i in list_of_integers:
        if i > peak:
            peak = i

    return peak
