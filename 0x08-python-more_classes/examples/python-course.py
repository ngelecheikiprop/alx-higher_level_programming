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
    print(f"{number}:{text}")

#third example

