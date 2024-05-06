#!/usr/bin/python3
"""This module has example 0
from https://python-course.eu/oop/properties-vs-getters-and-setters.php
"""


class P:

    def __init__(self, x):
        self.set_x(x)

    def get_x(self):
        return self.__x

    def set_x(self, x):
        if x < 0:
            self._x = 0
        elif x > 1000:
            self.__x = x
        else:
            self.__x = x

        x = property(get_x, set_x)
