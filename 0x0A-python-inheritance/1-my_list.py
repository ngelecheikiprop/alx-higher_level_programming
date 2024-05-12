#!/usr/bin/python3
"""Holds the class MyList that inherits from list"""


class MyList(list):
    """child of list"""

    def print_sorted(self):
        """sorts the instance of the list"""
        list_copy = self.copy()
        list_copy.sort()
        print(list_copy)
