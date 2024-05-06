#!/usr/bin/python3
"""static methods example in
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

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

import datetime
my_date = datetime.date(2016, 7, 10)
print(Employee.is_workday(my_date))
