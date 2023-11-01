#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
numcpy = number
if (numcpy < 0):
    numcpy = numcpy * -1
lst_dgt = numcpy % 10
if (lst_dgt > 5):
    print("Last digit of {} is {} and is greater than 5".format(number, lst_dgt), end="\n")
elif (lst_dgt == 0):
    print("Last digit of {} is {} and is 0".format(number, lst_dgt), end="\n")
elif ((lst_dgt < 6) and (lst_dgt != 0)):
    print("Last digit of {} is {} and is less than 6 and not 0".format(number, lst_dgt), end="\n")
