#!/usr/bin/python3

import add_0 as add_module

if __name__ == "__main__":
    a = 1
    b = 2
    result = add_module.add(a, b)
    print(
            "{a_val} + {b_val} = {result}"
            .format(a_val=a, b_val=b, result=result)
            )
