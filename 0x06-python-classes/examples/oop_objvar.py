#!/usr/bin/python3
class Robot:
    """represents a robot, with a name"""
    population = 0

    def __init__(self,name):
        self.name = name
        print("intializing {}".format(self.name))
        Robot.population += 1

    def die(self):
        print("{} is dieing".format(self.name))
        Robot.population -= 1

        if Robot.population == 0:
            print("{} was the last robot".format(self.name))
        else:
            print("There are still {} robots working".format(Robot.population))

    def say_hi(self):
        """ Greetings by the robot"""
        print("hi the masters call me {}".format(self.name))

    @classmethod
    def how_many(cls):
        '''say the number of robots'''
        print("we are {} of us".format(cls.population))
droid1 = Robot("R2-D2")
droid1.say_hi()
Robot.how_many()

droid2 = Robot("kk")
droid2.say_hi()

droid1.die()
droid2.die()
