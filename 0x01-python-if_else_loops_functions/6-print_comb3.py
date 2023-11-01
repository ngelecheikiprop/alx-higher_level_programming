#!/usr/bin/python3
j = 1
i = 0
while (i <= 100):
    if (i < 99):
        if ((i % 10) == 0):
            i = i + j
            j += 1
            if (i >= 100):
                continue
            if (i == 89):
                print("{:02d}".format(i), end='\n')
                break
        print("{:02d}".format(i), end=', ')
    i += 1
