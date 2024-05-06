#!/usr/bin/python3
"""This is amodule in youtube on class
and static methods
https://www.youtube.com/watch?v=rq8cL2XMM5M
"""


class Employee:

    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@gmail.com'
        self.pay = pay

        Employee.num_of_emps += 1

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amt = amount
   
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

emp_1 = Employee('david', 'kiprop', 10000)
emp_2 = Employee('mary', 'jemu', 20000)

Employee.set_raise_amount(1.05)

#print(Employee.raise_amt)
#print(emp_1.raise_amt)
#print(emp_2.raise_amt)

emp_3 = Employee.from_string("kip-ngel-5000")
print(emp_3.email)
print(emp_3.pay)
