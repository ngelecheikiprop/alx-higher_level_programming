#!/usr/bin/python3
"""This are examples from the youtube playlist - learn to program
https://www.youtube.com/watch?v=1AGyBuVCTeE
"""
import math
import random


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

#Warriors fight now

class Warrior:

    def __init__(self, name="Warrior", health=0, attkMax=0, blockMax=0):
        self.name = name
        self.health = health
        self.attkMax = attkMax
        self.blockMax = blockMax

    def attack(self):
        attkAmt = self.attkMax * (random.random() + .5)
        return attkAmt

    def block(self):
        blockAmt = self.blockMax * (random.random() + .5)
        return blockAmt

class Battle:
    def startFight(self, warior1, warior2):
        while True:
            if self.getAttackResult(warior1, warior2) == "Game Over":
                print("Game Over")
                break
            if self.getAttackResult(warior2, warior1) == "Game Over":
                print("Game Over")
                break

    @staticmethod
    def getAttackResult(wariorA, wariorB):
        wariorAAttkAmt = wariorA.attack()
        wariorBblockAmt = wariorB.block()

        damage2wariorB = math.ceil(wariorAAttkAmt- wariorBblockAmt)

        wariorB.health = wariorB.health - damage2wariorB

        print("{} atacks {} and deals {}".format(wariorA.name, wariorB.name, damage2wariorB))
        print("{} is down to {} health".format(wariorB.name, wariorB.health))

        if wariorB.health <= 0:
            print("{} has died and {} is victrious".format(wariorB.name, wariorA.name))
            return "Game Over"
        else:
            return "Fight Again"

maxi = Warrior("Maxi", 50, 20, 10)
glax = Warrior("Glax", 50, 20, 10)

battle = Battle()
battle.startFight(maxi, glax)