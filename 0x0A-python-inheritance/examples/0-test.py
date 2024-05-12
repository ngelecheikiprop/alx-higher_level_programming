#!/usr/bin/python3

class Person(object):
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def display(self):
        print(self.name, self.id)


emp = Person("Satyam", 102)
emp.display()
