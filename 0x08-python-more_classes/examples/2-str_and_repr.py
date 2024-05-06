#!/usr/bin/python3
"""when repr is the onlu one available what happens?"""


class A:
    def __repr__(self):
        return "42"

a = A()
print(str(a))
print(repr(a))
