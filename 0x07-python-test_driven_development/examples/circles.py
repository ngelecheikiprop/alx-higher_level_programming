#!/usr/bin/python3
from math import pi
def circle_area(r):
    if r < 0:
        raise ValueError("the radius cannot be negative.")
    if type(r) not in [int, float]:
        raise TypeError("The radius must be a non negative real number")
    return pi*(r**2)

