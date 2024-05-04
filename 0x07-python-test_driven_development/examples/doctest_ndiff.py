#!/usr/bin/python3

#doctest_ndiff.py

def my_function(a, b):
    """"
    >>> my_function(2, 3) #doctest: +REPORT_NDIFF
    6 
    """
    return a * b
