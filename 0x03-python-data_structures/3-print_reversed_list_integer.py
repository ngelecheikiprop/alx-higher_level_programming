#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    i = 0
    j = -1
    while (i < len(my_list)):
        print("{:d}".format(my_list[j]), end="\n")
        j -= 1
        i += 1
