#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    key1 = list(a_dictionary)[0]
    large = a_dictionary[key1]
    for key in list(a_dictionary):
        if a_dictionary[key] > large:
                large_key = key
    return large_key
