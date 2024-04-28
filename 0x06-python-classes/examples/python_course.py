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

#using the propoerty decorator
print("#using the propoerty decorator")
print("-------------------")
class P:

    def __init__(self, x):
        self.x = x

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if x < 0:
            self.__x = 0
        elif x > 1000:
            self.__x = 1000
        else:
            self.__x = x

p1 = P(1001)
print(p1.x)
print("wooow")