#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

#modulus with 10 and store in last digit
lst_dgt = number % 10
#check if lst_dgt > 5
if (lst_dgt > 5):
	print("Last digit of {} is {} and is greater than 5\n".format(number,lst_dgt))
#check if == 0
elif (lst_dgt == 0):
	print("Last digit of {} is {} and is 0\n".format(number,lst_dgt))
#check if less than 6 and not 0
elif ((lst_dgt < 6) and (lst_dgt != 0)):
	print("Last digit of {} is {} and is less than 6 and not 0\n".format(number,lst_dgt))
