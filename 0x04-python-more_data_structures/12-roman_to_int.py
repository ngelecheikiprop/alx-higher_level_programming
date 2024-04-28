#!/usr/bin/python3
def roman_to_int(roman_string):
    number = 0
    roman_dict =  {"I":1,"V":5, "X":10,"L":50, "C":100, "D":500, "M":1000}

    i = 0
    while i < len(roman_string):
        value = roman_dict[roman_string[i]]
        if(i + 1 < len(roman_string)):
            next_value = roman_dict[roman_string[i + 1]]
        else:
            next_value = 0
        if (next_value > value):
            number -= value
        else:
            number += value
        i += 1
    '''
    if "IV" in roman_string or "IX" in roman_string:
        number = number -2
    for c in roman_string:
        value = roman_dict[c]
        number += value
    '''
    return number
