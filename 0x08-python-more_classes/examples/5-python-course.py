#!/usr/bin/python3
""" example on Class Methods vs. Static Methods and Instance Methods
in python-course.eu
"""


class Pet:
    _class_info = "pet animals"

    def about(self):
        print("this class is about " + self._class_info + "!")

class Dog(Pet):
    _class_info = "man's best friends"

class Cat(Pet):
    _class_info = "all kinds of cats"

p = Pet()
p.about()
d = Dog()
d.about()
c = Cat()
c.about()
