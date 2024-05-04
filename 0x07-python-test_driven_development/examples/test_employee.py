#!/usr/bin/python3
import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("setupclass")

    @classmethod
    def tearDownClass(cls):
        print("tear downclass")

    def setUp(self):
        print("setup")
        self.emp_1 = Employee('kip', 'ngel', 10000)
        self.emp_2 = Employee('chem', 'mary', 2000)

    def tearDown(self):
        print("tear down")
        pass
        
    def test_email(self):
        print("test email")
        self.assertEqual(self.emp_1.email, 'kipngel@gmail.com')
        self.assertEqual(self.emp_2.email, 'chemmary@gmail.com')


if __name__=='__main__':
    unittest.main()
