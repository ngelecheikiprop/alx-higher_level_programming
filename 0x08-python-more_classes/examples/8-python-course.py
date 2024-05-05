#!/usr/bin/python3
"""Module has another example on
class method in https://python-course.eu/oop/class-instance-attributes.php
"""


class Person:
    total_people = 0

    def __init__(self, name):
        self.name = name
        Person.total_people += 1

    @classmethod
    def display_total_people(cls):
        print("Total number of people:", cls.total_people)

person1 = Person("kiprop")
person2 = Person("Chem")
person3 = Person("Kibenje")

Person.display_total_people()
