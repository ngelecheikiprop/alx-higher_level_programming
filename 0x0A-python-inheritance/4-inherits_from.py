#!/usr/bin/python3
"""function that checks what an object inherits from"""


def inherits_from(obj, a_class):
    """checks if a_class is parent of obj"""

    return issubclass(obj, a_class)
