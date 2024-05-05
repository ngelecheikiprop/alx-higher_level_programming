#!/usr/bin/python3
""" atatic methods from python-course.eu"""


class Robot:
    __counter = 0

    def __init__(self):
        type(self).__counter += 1

    def RobotInstances(self):
        return Robot.__counter

if __name__=="__main__":
    x = Robot()
    print(x.RobotInstances())
    y = Robot()
    print(y.RobotInstances())
