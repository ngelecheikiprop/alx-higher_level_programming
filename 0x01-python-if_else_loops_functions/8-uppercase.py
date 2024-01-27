#!/usr/bin/python3
def uppercase(str):
    for letter in str:
        if (ord(letter) >= 97 and ord(letter) <= 122):
            offset = ord(letter) - 97
            letter = chr(65 + offset)
        print(letter, end="")
    print()
