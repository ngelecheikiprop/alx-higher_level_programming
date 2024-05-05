#!/usr/bin/python3
"""This module is examples from:
https://python-course.eu/oop/class-instance-attributes.php
"""


class A:
    """First simple examples"""
    a = "I am a class attribute"

x = A()
y = A()
#print(x.a)
#print(y.a)
x.a = "this is instanve variable for x"
#print(x.a)
A.a = "this is changing a class attribute"
#print(A.a)
#print(x.a)

#secend class example
class Robot:
    Three_Laws = (
"""A robot may not injure a human being or, through inaction, allow a human being to come to harm.""",
"""A robot must obey the orders given to it by human beings, except where such orders would conflict with the First Law.,""",
"""A robot must protect its own existence as long as such protection does not conflict with the First or Second Law."""
)
    def __init__(self, name, build_year):
        self.name = name
        self.build_year = build_year

for number, text in enumerate(Robot.Three_Laws):
    #print(f"{number}:{text}")
    pass

#third example tried myslef
class Car:
    counter = 0
    def __init__(self, name):
        self.name = name
        Car.counter += 1
        #print("just made {}".format(self.name))

    def sell_car(self):
        Car.counter -= 1
        #print("sold {}".format(self.name))

lambo = Car("lambo")
audi = Car("audi")
#print("expecting two cars")
#print(Car.counter)
lambo.sell_car()
#print(Car.counter)
audi.sell_car()
#print(Car.counter)

#third example in tutorial
class C:

    counter = 0

    def __init__(self):
        type(self).counter += 1

    def __del__(self):
        type(self).counter -= 1

x = C()
print(C.counter)
y = C()
print(C.counter)
del x
print(C.counter)
del y
print(C.counter)
