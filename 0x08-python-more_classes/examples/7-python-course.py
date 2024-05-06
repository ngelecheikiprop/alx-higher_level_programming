#!/usr/bin/python3
"""this method has example on class method
from https://python-course.eu/oop/class-instance-attributes.php
"""


class Pet:
    _class_info = "Pet animals"

    @classmethod
    def about(cls):
        print("this class is about " + cls._class_info +"!")

class Dog(Pet):
    _class_info = "man's best friend"

class Cat(Pet):
    _class_info = "all kinds of cat"

Pet.about()
Dog.about()
Cat.about()
