#!/usr/bin/python3

from add_0 import add

if __name__ == "__main__":
    a = 1
    b = 2
    result = add(a, b)
    print(
            "{a_val} + {b_val} = {result}"
            .format(a_val=a, b_val=b, result=result)
            )
