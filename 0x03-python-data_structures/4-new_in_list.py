#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    my_copy = []
    if (idx < 0):
        return my_list
    if (idx > len(my_list) - 1):
        return my_list
    i = 0
    while (i < len(my_list)):
        if (idx == i):
            my_copy.append(element)
            i += 1
            continue
        my_copy.append(my_list[i])
        i += 1
    return my_copy
