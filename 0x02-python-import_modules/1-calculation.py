#!/usr/bin/python3

from calculator_1 import add, sub, mul, div


def perform_operations():
    a = 10
    b = 5
    add_result = add(a, b)
    sub_result = sub(a, b)
    mul_result = mul(a, b)
    div_result = div(a, b)

    print("{} + {} = {}".format(a, b, add_result))
    print("{} - {} = {}".format(a, b, sub_result))
    print("{} * {} = {}".format(a, b, mul_result))
    print("{} / {} = {}".format(a, b, div_result))


if __name__ == "__main__":
    perform_operations()
