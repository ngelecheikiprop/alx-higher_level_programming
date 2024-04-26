#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    if (len(sentence) > 0):
        fcharacter = sentence[0]
    else:
        fcharacter = None
    return (length, fcharacter)
