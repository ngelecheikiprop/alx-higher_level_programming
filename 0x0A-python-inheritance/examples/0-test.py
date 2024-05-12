#!/usr/bin/python3

class Person(object):
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def display(self):
        print(self.name, self.id)


# emp = Person("Satyam", 102)
# emp.display()

class Emp(Person):

    def print(self):
        print("Emp class called")


emp_details = Emp("Maynak", 103)

emp_details.display()
emp_details.print()
