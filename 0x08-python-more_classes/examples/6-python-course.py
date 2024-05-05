#!/usr/bin/python3
"""the secend example on Class Methods vs. Static Methods and Instance Methods
in https://python-course.eu/oop/class-instance-attributes.php
"""


class Pet:
    _class_info = "pet animals"

    @staticmethod
    def about():
        print("this class is about " + Pet._class_info + "!")

class Dog(Pet):
    _class_info = "man's best friend"

class Cat(Pet):
    _class_info = "all types of cats."

Pet.about()
Dog.about()
Cat.about()
