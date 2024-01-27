#!/usr/bin/python3
'''offset = 2;
for num in range(1,100):
    if (num % 10 == 0):
        num += offset
        offset += 1
    else:
        num += offset
    if (num < 90):
        print(num)
    else:
        break'''
printed = 0
for i in range(10):
    for j in range(i+1, 10):
        if (i == 8 and j == 9):
            print("{}{}".format(i, j))
        else:
            print("{}{}, ".format(i, j), end="")
