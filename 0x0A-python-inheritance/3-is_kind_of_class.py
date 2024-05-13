#!/usr/bin/python3
"""function that checks if object is an
intsance of or from a class that inherited from it"""


def is_kind_of_class(obj, a_class):
    """checkf if obj is child or grandchilf 0f a_class"""
    return isinstance(obj, a_class)
