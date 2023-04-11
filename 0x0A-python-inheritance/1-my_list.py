#!/usr/bin/python3

"""Exports a class MyList that inherits from list."""


class MyList(list):
    """Inherits from the built in list object."""
    def __init__(self):
        self.my_list = []

    def __str__(self):
        return str(self.my_list)

    def append(self, item):
        self.my_list.append(item)

    def print_sorted(self):
        new_list = self.my_list.copy()
        sorted_list = []
        min_in_list = new_list[0]

        while True:
            for i in new_list:
                if i < min_in_list:
                    min_in_list = i

            sorted_list.append(min_in_list)
            new_list.remove(min_in_list)
            if len(new_list) == 0:
                break
            else:
                min_in_list = new_list[0]
        
        print(sorted_list)
