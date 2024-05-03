#!/usr/bin/python3
class MyClass:
    pass

def unpredictable(obj):
    """
        Returns a new list containing

        >>> unpredictable(MyClass())#doctest: +ELLIPSIS
        [<doctest_ellipsis.MyClass object at 0x...>]
    """
    return[obj]

