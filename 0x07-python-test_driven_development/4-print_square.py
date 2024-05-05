#!/usr/bin/python3
"""
This module hosts a function:
    print_square - that prints a square with #
                    character
"""


def print_square(size):
    """Prints a square with # given its size
    Args:
        size (int): the size  of the square
    Returns:
        prints the square
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
