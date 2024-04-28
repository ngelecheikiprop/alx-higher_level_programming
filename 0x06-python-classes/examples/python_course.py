#!usr/bin/python3
class P:
    def __init__(self, x):
        self.__x = x
    def set_x(self, x):
        self.__x = x
    def get_x(self):
        return self.__x
p1 = P(42)
p2 = P(100)
print( p1.get_x())

p1.set_x(47)
print( p1.get_x())