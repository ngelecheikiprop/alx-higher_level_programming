#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    od_set = []
    for x in set_1:
        if x not in set_2:
            od_set.append(x)
    for x in set_2:
        if x not in set_1:
            od_set.append(x)
    return od_set
