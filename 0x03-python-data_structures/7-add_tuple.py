#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    val_1 = tuple_a[0] if len(tuple_a) >= 1 else 0
    val_2 = tuple_b[0] if len(tuple_b) >= 1 else 0
    val_3 = tuple_a[1] if len(tuple_a) >= 2 else 0
    val_4 = tuple_b[1] if len(tuple_b) >= 2 else 0
    result_1 = val_1 + val_2
    result_2 = val_3 + val_4

    return (result_1, result_2)
