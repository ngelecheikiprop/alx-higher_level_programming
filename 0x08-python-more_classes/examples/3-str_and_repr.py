#!/usr/bin/python3
"""this module is the last example on
https://python-course.eu/oop/object-oriented-programming.php
in topi str and repr methods"""


class Robot:
    def __init__(self, name, build_year):
        self.name = name
        self.build_year = build_year

    def __repr__(self):
        return "Robot('" + self.name+ "',"+ str(self.build_year) + ")"

if __name__ == "__main__":
    x = Robot("kiprop", 1999)
    x_str = str(x)
    print(x_str)
    print("type of str" , type(str))
    new  = eval(x_str)
    print(new)
    print("type of new:", type(new))
