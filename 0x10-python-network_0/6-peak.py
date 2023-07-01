#!/usr/bin/python3
""" Find peak module """

def find_peak(list_of_integers):
    """ finds a peak in a list of unsorted integers """
    if len(list_of_integers) < 1:
        return None

    mid = int(len(list_of_integers) / 2)
    if list_of_integers[mid] >= list_of_integers[mid + 1]\
            and list_of_integers[mid] >= list_of_integers[mid - 2]:
        return list_of_integers[mid]

    right = find_right_peak(list_of_integers, mid + 1)
    left = find_left_peak(list_of_integers, mid - 1)
    if right:
        return right
    elif left:
        return left
    else:
        return None


def find_right_peak(arr, i):
    """ find peak on the right """
    if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
        return arr[i]

    return find_right_peak(arr, i + 1)


def find_left_peak(arr, i):
    """ find peak on left """
    if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
        return arr[i]

    return find_left_peak(arr, i - 1)
