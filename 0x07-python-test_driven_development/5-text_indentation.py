#!/usr/bin/python3
"""Has a  function:
    text_identation - prints a text with 2 new lines after each 
    of these characters: ., ? and :
    Args:
        the text to print
    Return:
        prints the idented text
"""


def text_indentation(text):
    if type(text) is not str:
        raise TypeError("text must be a string")
    for letter in text:
        print(letter, end="")
        if letter in ['.', '?', ':']:
            print()
            print()
