#!/usr/bin/python3
def element_at(my_list, idx):
    if (idx < 0):
        return None
    if (idx > (len(my_list) - 1)):
        return None
    i = 0
    while (i < len(my_list)):
        if (idx == i):
            return my_list[i]
        i += 1
