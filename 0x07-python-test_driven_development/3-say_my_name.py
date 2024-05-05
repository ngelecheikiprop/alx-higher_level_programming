#!/usr/bin/python3
""" this module has a function
that says my name
"""


def say_my_name(first_name, last_name=""):
    """This function says your name
    Args:
        first name - your first name
        last_name - your last name
    Return:
        - nothinig but prints your name
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
