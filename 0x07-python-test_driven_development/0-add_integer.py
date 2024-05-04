#!/usr/bin/python3
"""This module has the function 0-add_integer add_integer
to do addition.
a function that adds 2 integers.
Prototype: def add_integer(a, b=98):
"""


def add_integer(a, b=98):
    """a function that adds 2 integers.
    Args : a, b whis is 98 by defualt
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")

    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")

    if type(a) is float:
        a = int(a)

    if type(b) is float:
        b = int(b)

    return a + b

