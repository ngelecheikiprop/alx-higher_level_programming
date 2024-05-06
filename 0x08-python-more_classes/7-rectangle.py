#!/usr/bin/python3
""" Add feature to rectangle for changing the print symbol"""


class Rectangle:
    """my rectangle class"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be an integer")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__height + self.__width)

    def __str__(self):
        if self.__height == 0 or self.__width == 0:
            return ""
        string = ""
        for i in range(self.__height):
            for j in range(self.__width):
                string += str(self.print_symbol)
            string += "\n"
        return string

    def __repr__(self):
        return "Rectangle(" + str(self.__width) + "," + str(self.__height) + ")"
    def __del__(self):
        print("Bye rectangle...")
        type(self).number_of_instances -= 1
