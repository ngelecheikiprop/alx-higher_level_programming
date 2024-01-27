#!/usr/bin/python3
printed = 0
for num in range(0, 100):
    if (num == 99):
        print("{0:02d}".format(num))
    else:
        print("{0:02d}, ".format(num), end="")
