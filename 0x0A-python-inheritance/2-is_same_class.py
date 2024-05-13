#!/usr/bin/python3
"""holds a function to check if objects are of same class"""


def is_same_class(obj, a_class):
    if type(obj) is a_class:
        return True
    else:
        return False
