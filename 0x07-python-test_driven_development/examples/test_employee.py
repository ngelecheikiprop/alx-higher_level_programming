#!/usr/bin/python3
import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):

    def test_email(self):
        emp_1 = Employee('kip', 'ngel', 10000)
        emp_2 = Employee('chem', 'mary', 2000)

        self.assertEqual(emp_1.email, 'kipngel@gmail.com')
        self.assertEqual(emp_2.email, 'chemmary@gmail.com')


if __name__=='__main__':
    unittest.main()
