#!/usr/bin/python3
"""This are examples from the youtube playlist - learn to program
https://www.youtube.com/watch?v=1AGyBuVCTeE
"""
class Dog:
    def __init__(self, name="", height=0, weight=0):
        self.name = name
        self.height = height
        self.weight = weight

    def run(self):
        print("{} the dog runs".format(self.name))
    def eat(self):
        print("{} the dog eats".format(self.name))
    def barks(self):
        print("{} the dog barks".format(self.name))

spot = Dog("Spot", 66,26)
spot.barks()

bowser = Dog()
bowser.barks()


class Square:

    def __init__(self, height="0", width="0"):
        self.height = height
        self.width = width

    @property
    def height(self):
        print("Retrieving the heigh")
        return self.__height

    @height.setter
    def height(self, value):
        if value.isdigit():
            self.__height = value
        else:
            print("enter a number for height")

    def width(self):
        print("Retrieving the heigh")
        return self.__width

    @height.setter
    def width(self, value):
        if value.isdigit():
            self.__width = value
        else:
            print("enter a number for height")

    def get_area(self):
        return int(self.__height) * int(self.__width)

asquare = Square()

asquare.height = input("enter height :")
asquare.width = input("enter width : ")

print("area of {} by {} is {}".format(asquare.height, asquare.width, asquare.get_area()))