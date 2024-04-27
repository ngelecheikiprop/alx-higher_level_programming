#!/usr/bin/python3
def common_elements(set_1, set_2):
    c_set = []
    for x in set_1:
        for y in set_2:
            if x == y:
                c_set.append(x)
    return c_set
