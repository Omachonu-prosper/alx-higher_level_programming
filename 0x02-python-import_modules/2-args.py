#!/usr/bin/python3

import sys


def print_args():
    argv = sys.argv
    argv_count = len(argv) - 1
    arg_or_args = "argument" if argv_count == 1 else "arguments"
    end_of_line = "." if argv_count == 0 else ":"

    print(
            "{argv_count} {arg_or_args}{end_of_line}"
            .format(
                argv_count=argv_count,
                arg_or_args=arg_or_args,
                end_of_line=end_of_line
            )
    )

    for i in range(1, argv_count + 1):
        print("{i}: {arg}".format(i=i, arg=argv[i]))


if __name__ == "__main__":
    print_args()
